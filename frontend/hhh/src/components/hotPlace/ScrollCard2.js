import React from "react";
import GuCard from "./GuCard";
import axios from "axios";
import CardPlace from "./CardPlace";
import CardStore from "./CardStore";
import "./ScrollCard2.scss";
import Header from "../common/Header";

const area = window.location.href.split("/")[4];
const username = sessionStorage.getItem("username");
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
        console.log(res);
        this.setState({
          storeList: res.data,
        });
      });

    // await axios
    //   .get("http://13.125.113.171:8000/places/location/")
    //   .then((res) => {
    //     this.setState({
    //       locList: res.data.results,
    //     });
    //   });
  }

  render() {
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
                <CardStore state={slist} />
              ))}
              {/* {this.state.locList.map((plist) => (
              <CardPlace state={plist} />
            ))} */}
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default ScrollCard2;
