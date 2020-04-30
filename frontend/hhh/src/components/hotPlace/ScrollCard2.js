import React from "react";
import GuCard from "./GuCard";
import axios from "axios";
import CardStore from "./CardStore";
import "./ScrollCard2.scss";
import Header from "../common/Header";

const area = window.location.href.split("/")[4];
const username = sessionStorage.getItem("username")
  ? sessionStorage.getItem("username")
  : "Eum_mericano";

class ScrollCard2 extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      storeList: [],
      locList: [],
    };
  }

  async componentDidMount() {
    await axios
      .get(`http://13.125.113.171:8000/recommend/${area}/${username}`)
      .then((res) => {
        this.setState({
          storeList: res.data,
        });
      });
  }

  render() {
    console.log(this.state.storeList);
    return (
      <>
        <Header />
        <br />
        <div className="scrollContainer">
          <div className="logo">
            <GuCard area={area} />
          </div>
          <div className="container">
            <div className="container2">
              {this.state.storeList.map((slist) => (
                <CardStore state={slist} area={area} />
              ))}
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default ScrollCard2;
