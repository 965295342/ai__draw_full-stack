import { title } from "@/components/primitives";
import DefaultLayout from "@/layouts/default";
import {Input} from "@nextui-org/input";
// import ReactECharts from 'echarts-for-react';
import { SetStateAction, useState,useEffect , useRef,useMemo} from "react";
import axios from 'axios';
// import * as echarts from 'echarts';
// import {Card, CardBody} from "@nextui-org/react";
import EChartsComponent from './chart'
const PlotPage :React.FC = () =>  {
  const [inputValue, setInputValue] = useState("");
  const [xData, setXData] = useState<number[]>([]);
  const [yData, setYData] = useState<number[]>([]);
  const handleChange = (e: { target: { value: SetStateAction<string>; }; }) => {
    setInputValue(e.target.value);
  };
  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://110.42.239.93:8553/api/plot", {
        method: "POST",
        headers: {
          // "Content-Type": "application/json",
          "Content-Type": "text/javascript",
        },
        // body: JSON.stringify({ command: inputValue })
        command:inputValue
      });
      const { x, y } = response.data;
      console.log(y); 
      console.log(inputValue); 
      setXData(x);
      setYData(y);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  
  const options = useMemo(() => ({
    title: {
      text: 'graph',
    },
    tooltip: {},
    xAxis: {
      data: xData,
    },
    yAxis: {},
    series: [
      {
        name: '系列 2',
        type: 'line',
        data: yData,
        smooth: true,
        lineStyle: {
          color: '#FF8800',
        },
      },
    ],
  }), [xData, yData]);  // 依赖项，只有xData或yData改变时才会重新计算
  // setTimeout(() => {
  //   console.log('这行代码将在1秒后执行');
  // }, 1000); // 1000 毫秒 = 1 秒
  return (
    <DefaultLayout>
      <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
        <div className="inline-block max-w-lg text-center justify-center">
          <h1 className={title()}>Plot</h1>
        </div>
        <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
        <Input type="text" label="function"placeholder="Enter your function"             value={inputValue}
            onChange={handleChange} />
        <button onClick={handleSubmit} className="btn-primary">
            Submit
          </button>
          {/* { <ChartComponent />} */}
      </div>
      <div id="main"className="flex w-full flex-wrap md:flex-nowrap gap-4" > 
      <EChartsComponent option={options}></EChartsComponent>
      </div>
      </section>
    </DefaultLayout>
  );
}


export default PlotPage;