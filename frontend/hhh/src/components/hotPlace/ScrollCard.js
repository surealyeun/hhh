import React, { Component, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import ScrollMenu from "react-horizontal-scrolling-menu";
import "./ScrollCard.scss";
import GuCard from './GuCard';

const LocItem = ({
  id,
  location_name,
  address_see,
  address_gu,
  address_dong,
  tel,
  latitude,
  longitude,
  description,
  url,
}) => {
  return (
    <div className="container">
      <div className="grid">
        <Link
          to={{
            pathname: `/place/${id}`,
            state: {
              location_name,
              description,
              address_see,
              address_gu,
              address_dong,
              latitude,
              longitude,
            },
          }}
        >
          <figure className="effect-kira">
            <img src={url} width="630px" height="400px" />
            <figcaption>
              <h2 style={{ color: "#fff" }}>
                <span className="inner-span">{location_name}</span>
              </h2>

              <p style={{ margin: "20px" }}>{description}</p>
            </figcaption>
          </figure>
        </Link>
      </div>
    </div>
  );
};

const MenuItem = ({
  id,
  store_name,
  branch,
  area,
  tel,
  address_see,
  address_gu,
  address_dong,
  latitude,
  longitude,
  category,
  url,
}) => {
  return (
    <div className="container">
      <div className="grid">
        <Link
          to={{
            pathname: `/store/${id}`,
            state: {
              store_name,
              category,
              address_see,
              address_gu,
              address_dong,
              latitude,
              longitude,
            },
          }}
        >
          <figure className="effect-kira">
            <img src={url} width="630px" height="400px" />
            <figcaption>
              <h2 style={{ color: "#fff" }}>
                <span className="inner-span">{store_name}</span>
              </h2>

              <p style={{ margin: "20px" }}>{category}</p>
            </figcaption>
          </figure>
        </Link>
      </div>
    </div>
  );
};

export const Loc = (list) =>
  list.map((el) => {
    const {
      id,
      location_name,
      address_see,
      address_gu,
      address_dong,
      tel,
      latitude,
      longitude,
      description,
    } = el;

    return (
      <LocItem
        id={id}
        location_name={location_name}
        address_see={address_see}
        address_gu={address_gu}
        address_dong={address_dong}
        tel={tel}
        latitude={latitude}
        longitude={longitude}
        description={description}
        url="https://img.hankyung.com/photo/201709/01.14677326.1.jpg"
        key={location_name}
      />
    );
  });

// All items component
// Important! add unique key
export const Menu = (list) =>
  list.map((el) => {
    const {
      id,
      store_name,
      branch,
      area,
      tel,
      address_see,
      address_gu,
      address_dong,
      latitude,
      longitude,
      category,
    } = el;

    return (
      <MenuItem
        id={id}
        store_name={store_name}
        branch={branch}
        area={area}
        tel={tel}
        address_see={address_see}
        address_gu={address_gu}
        address_dong={address_dong}
        latitude={latitude}
        longitude={longitude}
        category={category}
        url="https://bit.ly/2V93eDV"
        key={store_name}
      />
    );
  });

const selected = "item1";

class ScrollCard extends Component {
  constructor(props) {
    super(props);

    this.state = {
      storeList: [],
      locList: [],
    };
  }

  async componentDidMount() {
    await axios.get("http://13.125.113.171:8000/dining/stores/").then((res) => {
      this.menuItems = Menu(res.data.results, selected);

      this.setState({
        storeList: res.data.results,
      });
    });

    await axios
      .get("http://13.125.113.171:8000/places/location/")
      .then((res) => {
        this.locItems = Loc(res.data.results, selected);

        this.setState({
          locList: res.data.results,
        });
      });
  }

  state = {
    selected,
  };

  onSelect = (key) => {
    this.setState({ selected: key });
  };

  render() {
    const { selected } = this.state;
    // Create menu from items
    const menu = this.menuItems;
    const loc = this.locItems;

    return (
      <div className="scrollContainer">
        <GuCard/>
        <div className="scrollPlace">
          <ScrollMenu
            data={menu}
            selected={selected}
            onSelect={this.onSelect}
          />
          <ScrollMenu data={loc} selected={selected} onSelect={this.onSelect} />
        </div>
      </div>
    );
  }
}

export default ScrollCard;
