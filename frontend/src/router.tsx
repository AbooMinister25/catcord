import * as React from "react";

import {
  BrowserRouter,
  Route,
  Switch,
} from "react-router-dom";

import Home from "./pages/Home";
import { NotFound } from "./pages/404";

export function Router(): JSX.Element {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="*" component={NotFound} />
      </Switch>
    </BrowserRouter>
  );
}