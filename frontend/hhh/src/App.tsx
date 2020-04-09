import React from 'react';

import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';
import Main from './components/main/Main';
// import ScrollCard from "./components/hotPlace/ScrollCard";
// import FeedList from './components/feedList/FeedList';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>

      {/* <ScrollCard />
      <FeedList></FeedList> */}
    </div>
  );
}

export default App;