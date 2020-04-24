import React from "react";
import GuCard from "./GuCard";
import axios from "axios";
import CardPlace from "./CardPlace";
import CardStore from "./CardStore";
import "./ScrollCard2.scss";

class ScrollCard2 extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      storeList: [],
      locList: [],
    };
  }

  async componentDidMount() {
    await axios.get("http://13.125.113.171:8000/dining/stores/").then((res) => {
      this.setState({
        storeList: res.data.results,
      });
    });

    await axios
      .get("http://13.125.113.171:8000/places/location/")
      .then((res) => {
        this.setState({
          locList: res.data.results,
        });
      });
  }

  render() {
    console.log(window.location.href.split('/')[4])
    return (
      <div className="scrollContainer">
        <div className="logo">
          <GuCard />
        </div>
        <div className="container">
          <div className="container2">
            {this.state.storeList.map((slist) => (
              <CardStore state={slist} />
            ))}
            {this.state.locList.map((plist) => (
              <CardPlace state={plist} />
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default ScrollCard2;
