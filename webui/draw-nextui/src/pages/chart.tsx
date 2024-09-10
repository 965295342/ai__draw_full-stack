import React, { useEffect, useRef } from 'react';
import * as echarts from 'echarts';

const EChartsComponent = ({ option }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    if (option && chartRef.current) {
      const myChart = echarts.init(chartRef.current);
      myChart.setOption(option);

      // 创建一个包装函数来调用 resize，确保不传递任何参数
      const handleResize = () => {
        myChart.resize();
      };

      window.addEventListener('resize', handleResize);

      return () => {
        window.removeEventListener('resize', handleResize);
        myChart.dispose();
      };
    }
  }, [option]); // 依赖于外部传入的 option

  return (
    <div ref={chartRef} style={{ width: '1200px', height: '500px' }}></div>
  );
};

export default EChartsComponent;