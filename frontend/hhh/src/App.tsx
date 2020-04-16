import React from 'react';

import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import Main from './components/main/Main';
import ScrollCard from "./components/hotPlace/ScrollCard";
import FeedList from './components/feedList/FeedList';
import userInfo from "./components/userInfo/userInfo";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Route path="/feedList" component={FeedList} />
          <Route path="/spotList" component={ScrollCard} />
          <Route path="/userinfo" component={userInfo} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;