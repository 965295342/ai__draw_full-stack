import { Route, Routes } from "react-router-dom";

import IndexPage from "@/pages/index";
import DocsPage from "@/pages/docs";
import PricingPage from "@/pages/pricing";
import BlogPage from "@/pages/blog";
// import AboutPage from "@/pages/about";
import PlotPage from "@/pages/plot";
// import * as echarts from 'echarts';
function App() {
  return (
    
    <Routes>
      <Route element={<PlotPage />} path="/" />
      <Route element={<DocsPage />} path="/docs" />
      <Route element={<PlotPage />} path="/plot" />
      <Route element={<PricingPage />} path="/pricing" />
      <Route element={<BlogPage />} path="/blog" />
      <Route element={<IndexPage />} path="/about" />
    </Routes>
  );
}

export default App;
