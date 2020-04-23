import React from "react";
import GuCard from "./GuCard";
import axios from "axios";
import Place from "./CardPlace";
import Place2 from "./CardStore";
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
    return (
      <div className="scrollContainer">
        <div className="container">
          <div className="container2">
            {this.state.locList.map((plist) => (
              <Place state={plist} />
            ))}
            {/* {this.state.storeList.map((slist) => (
              <Place2 state={slist} />
            ))} */}
          </div>
        </div>
      </div>
    );
  }
}

export default ScrollCard2;
