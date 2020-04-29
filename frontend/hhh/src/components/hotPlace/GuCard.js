import React from "react";
import axios from "axios";
import "./GuCard.scss";

class UserCard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {},
    };
  }
  
  async componentDidMount() {
    const areaURL = `http://13.125.113.171:8000/users/detail/${this.props.area}/`;
    let { data: user } = await axios.get(areaURL);
    this.setState({ user });
  }

  render() {
    return (
      <div id="Gu-card">
        <div id="avatar">
          <img src={`http://13.125.113.171:8000` + this.state.user.avatar} />
        </div>
        <div id="user-info">
          <div id="user-id">{this.state.user.last_name}</div>
          <div id="user-follow">
            <ul>
              <li>
                게시물 <b>30</b>
              </li>
              <li>
                팔로워 <b>21</b>
              </li>
              <li>
                팔로우 <b>29</b>
              </li>
            </ul>
          </div>
          <div id="user-desc">
            <b>{this.state.user.first_name}</b>
            {this.state.user.bio}
          </div>
        </div>
      </div>
    );
  }
}

export default UserCard;
