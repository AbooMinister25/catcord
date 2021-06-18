import React from "react";
import ReactDOM from "react-dom";
import '../sass/globals.sass'

function App(): JSX.Element {
  return (
    <div>
      <h1>Catcord</h1>
      <h2>The minimal, open source chat app</h2>
    </div>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
)