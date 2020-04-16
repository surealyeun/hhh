import React, { Component, useState } from "react";
import axios from 'axios';
import ScrollMenu from "react-horizontal-scrolling-menu";
import "./ScrollCard.scss";
import {
  HeartOutlined,
  PlusCircleOutlined,
  HeartFilled,
} from "@ant-design/icons";

const LocItem = ({ id, location_name, address_see, address_gu, address_dong, tel, latitude, longitude, description, url }) => {
  const [iconState, seticonState] = useState(true);

  return (
    <div className="container">
      <div className="grid">
        <figure className="effect-kira">
          <img src={url} width="630px" height="400px" />
          <figcaption>
            <h2 style={{ color: "#fff" }}>
              <span className="inner-span">{location_name}</span> {id}
            </h2>

            <p>
              {description}
              <a href="#">
                {iconState ? (
                  <HeartOutlined
                    onClick={() => seticonState(false)}
                    style={{ color: "#00b992" }}
                  />
                ) : (
                    <HeartFilled
                      onClick={() => seticonState(true)}
                      style={{ color: "#00b992" }}
                    />
                  )}
              </a>

              <a href="#">
                <PlusCircleOutlined />
              </a>
            </p>

            <p className="infos">번호: {tel}}</p>
            <p className="infos">시: {address_see}</p>
            <p className="infos">구: {address_gu}</p>
            <p className="infos">동: {address_dong}</p>
            <p className="infos">위도: {latitude}</p>
            <p className="infos">경도: {longitude}</p>
          </figcaption>
        </figure>
      </div>
    </div>
  );
}

// One item component
// selected prop will be passed
const MenuItem = ({ id, store_name, branch, area, tel, address, latitude, longitude, category_list, url }) => {
  // const initColor = "#eb2f96";
  // const myFunction = () => {
  //   this.twoToneColor = "#00b992";
  // }

  const [iconState, seticonState] = useState(true);

  return (
    <div className="container">
      <div className="grid">
        <figure className="effect-kira">
          <img src={url} width="630px" height="400px" />
          <figcaption>
            <h2 style={{ color: "#fff" }}>
              {category_list} <span className="inner-span">{store_name}</span> {id}
            </h2>

            <p>
              {address}({branch})
              <a href="#">
                {iconState ? (
                  <HeartOutlined
                    onClick={() => seticonState(false)}
                    style={{ color: "#00b992" }}
                  />
                ) : (
                    <HeartFilled
                      onClick={() => seticonState(true)}
                      style={{ color: "#00b992" }}
                    />
                  )}
              </a>

              <a href="#">
                <PlusCircleOutlined />
              </a>
            </p>

            <p className="infos">지역: {area}</p>
            <p className="infos">번호: {tel}</p>
            <p className="infos">위도: {latitude}</p>
            <p className="infos">경도: {longitude}</p>
          </figcaption>
        </figure>
      </div>
    </div>
  );
};

export const Loc = (list) =>
  list.map((el) => {
    const { id, location_name, address_see, address_gu, address_dong, tel, latitude, longitude, description } = el;

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
    const { id, store_name, branch, area, tel, address, latitude, longitude, category_list } = el;

    return (
      <MenuItem
        id={id}
        store_name={store_name}
        branch={branch}
        area={area}
        tel={tel}
        address={address}
        latitude={latitude}
        longitude={longitude}
        category_list={category_list}
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
      locList: []
    }

    // call it again if items count changes
  }

  async componentDidMount() {
    await axios.get('http://13.125.113.171:8000/dining/stores/')
      .then(res => {
        this.menuItems = Menu(res.data.results, selected);

        this.setState({
          storeList: res.data.results
        });
      });

    await axios.get('http://13.125.113.171:8000/places/location/')
      .then(res => {
        this.locItems = Loc(res.data.results, selected);

        this.setState({
          locList: res.data.results
        })
      })
  }

  state = {
    selected
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
      <div className="App">
        <ScrollMenu data={menu} selected={selected} onSelect={this.onSelect} />
        <ScrollMenu data={loc} selected={selected} onSelect={this.onSelect} />
      </div>
    );
  }
}

export default ScrollCard;
