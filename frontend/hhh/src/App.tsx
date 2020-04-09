import React from 'react';
import './App.scss';

import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import Main from './components/main/Main';
import ScrollCard from "./components/hotPlace/ScrollCard";
import FeedList from './components/feedList/FeedList';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Route path="/feedList" component={FeedList} />
          <Route path="/spotList" component={ScrollCard} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;