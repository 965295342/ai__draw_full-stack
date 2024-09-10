from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
from fastapi.middleware.cors import CORSMiddleware
from dify import DifyTool
import json
from prometheus_client import start_http_server, Summary
from cache import generate_cache_key,get_from_cache,store_in_cache
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
dify_tool = DifyTool()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中指定具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PlotCommand(BaseModel):
    command: str
    
@app.post("/api/plot")
async def plot(command: PlotCommand):
    try:
        # 确保写入文件时使用 UTF-8 编码
        return runCommand(command=command.command)

    except Exception as e:
         raise HTTPException(status_code=400, detail=e)
    
@REQUEST_TIME.time()    
def runCommand(command: str):
    # 生成缓存 key
    cache_key = generate_cache_key(command)
    
    # 检查 Redis 缓存是否有命中
    cached_code = get_from_cache(cache_key)
    
    if cached_code:
        print("Cache hit")
        code = cached_code
    else:
        print("Cache miss")
        # 使用 dify_tool 获取生成的代码
        code = dify_tool.get_answer(command)
        # 存储到 Redis 缓存
        store_in_cache(cache_key, code)

    # 直接通过 subprocess 执行代码
    result = subprocess.run(
        ['python', '-c', code],
        text=True,
        capture_output=True
    )

    output = result.stdout

    # 解析 JSON 字符串为字典
    try:
        result_json = json.loads(output)
        x = result_json.get("x")
        y = result_json.get("y")
        print(x)
        return {"x": x, "y": y}
    except json.JSONDecodeError:
        print("Error: Output is not valid JSON")
        return None
# def runCommand(command: str):
#     # 获取生成的代码
#     code = dify_tool.get_answer(command)
#     print(code)

#     # 使用 subprocess 调用 Python 解释器来执行这个脚本
#     result = subprocess.run(
#         ['python', '-c', code],  # 直接执行 Python 代码
#         text=True,
#         capture_output=True
#     )

#     # 捕获子进程的标准输出
#     output = result.stdout

#     # 解析 JSON 字符串为字典
#     try:
#         result_json = json.loads(output)
#         x = result_json.get("x")
#         y = result_json.get("y")
#         print(x)
#         return {"x": x, "y": y}
#     except json.JSONDecodeError:
#         print("Error: Output is not valid JSON")
#         return None


if __name__ == "__main__":
    import uvicorn
    start_http_server(8000)  # Start Prometheus endpoint
    print("hello world")
    uvicorn.run(app, host="0.0.0.0", port=8553)