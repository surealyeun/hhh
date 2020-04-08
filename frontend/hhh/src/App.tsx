import React from 'react';
import './App.css';

import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import Main from './components/main/Main';
import ScrollCard from "./components/hotPlace/ScrollCard";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>

      <ScrollCard />
    </div>
  );
}

export default App;