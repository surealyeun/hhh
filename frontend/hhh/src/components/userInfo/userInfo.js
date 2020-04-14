import React, { Component } from "react";
import axios from "axios";


const userUrl = `http://13.125.113.171:8000/users/detail/joker/`;

class userInfo extends Component {
  constructor(props) {
    super(props);
    this.state = { user: {} };
  }

  async componentDidMount() {
    let { data: user } = await axios.get(userUrl);
    this.setState({ user });
  }

  render() {
    const { user } = this.state;

    if (user) {
      return (
        <div>
          <form>
            <input type="text" value={user.username} />
          </form>
        </div>
      );
    } else {
      return <h3>empty user</h3>
    }
  }
}

export default userInfo;
