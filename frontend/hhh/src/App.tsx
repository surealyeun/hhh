import React from 'react';
import { BrowserRouter, Switch, Redirect, Route } from 'react-router-dom';

import Main from './components/main/Main';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;