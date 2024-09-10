from dify_client import CompletionClient
from config import load_config

class DifyTool:
    api_key = load_config("/.config/config.yaml")["dify-app"]["dify-key"]

    def get_answer(self,query):
        client = CompletionClient(self.api_key)

        c_response = client.create_completion_message(inputs={"query":query},response_mode="blocking",user = "user_id")
        c_response.raise_for_status()

        result = c_response.json()
        print(result)
        return result.get("answer")
d = DifyTool()
print(d.api_key)