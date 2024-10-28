import "./index.css"; // import css

import * as React from "react";
import { createRoot } from "react-dom/client";
import Header from "./components/Header";
import Dropzone from "./components/Dropzone";
import Button from "./components/Button";

const root = createRoot(document.getElementById("root") as HTMLElement);
root.render(
  <div className="app">
    <Header />
    <Dropzone />
    <Button />
  </div>
);
