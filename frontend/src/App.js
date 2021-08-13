import React from 'react';
import './App.less';
import { Homepage, Landingpage } from './Views';
import { Navbar } from './Components';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";


const App = () => (
  <div>
    <Router>
      <Navbar />
      <Switch>
        <Route path="/home">
          <Homepage />
        </Route>
        <Route exact path="/">
          <Landingpage />
        </Route>
      </Switch>
    </Router >
  </div>
);

export default App;