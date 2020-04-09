import React, { Component, useState } from "react";
import ScrollMenu from "react-horizontal-scrolling-menu";
import "./Kira.scss";
import {
  HeartOutlined,
  PlusCircleOutlined,
  HeartFilled,
} from "@ant-design/icons";

// list of items
const list = [
  {
    category: "ART",
    name: "D MUSEUM",
    description: "HIP 한 미술관",
    url:
      "https://www.daelimmuseum.org/front/images/exhibition/201908/img05.jpg",
  },
  {
    category: "SHOW",
    name: "이상한나라의앨리스 전시회",
    description: "도심 속 원더랜드",
    url: "https://img.hankyung.com/photo/201709/01.14677326.1.jpg",
  },
  {
    category: "SHOW",
    name: "UNDERSTAGE",
    description: "현대카드 공연 스테이지",
    url:
      "https://img.hyundaicard.com/cms_content/cp_culture/image/145052_BIG.png",
  },
  {
    category: "CAFE",
    name: "노스모크위드아웃파이어",
    description: "주택 안의 카페",
    url: "https://bit.ly/2V93eDV",
  },
  {
    category: "CAFE",
    name: "미실",
    description: "역사와 감성을 담은 카페",
    url:
      "https://post-phinf.pstatic.net/MjAxOTEwMDJfMTk2/MDAxNTY5OTk2NTQyMTE4.oj6DIG-f-6AR8rAvKLWsha89zXu2V-YgYNztYd_jtosg.z0C8hh-Atl30a93kB5Zj4HTmS0pS2dHwXq9kvT6IGWQg.JPEG/7._%EB%AF%B8%EC%8B%A4.jpg?type=w1200",
  },
  {
    category: "CAFE",
    name: "살라댕방콕",
    description: "한국 안의 작은 방콕",
    url:
      "https://mblogthumb-phinf.pstatic.net/MjAxOTA5MDVfMTY0/MDAxNTY3Njg2NTM5NDQz.lw-vFO8lU3R9vI4VIACflRp5nwAtSrWcl2XWIJsU5Swg.X0paFcdezEwEoEGoWLrjCno4Ns0GICoUVdvLXWgBd4Yg.JPEG.jy2_wj7/IMG_1422.JPG?type=w800",
  },
  {
    category: "CAFE",
    name: "미실",
    description: "역사와 감성을 담은 카페",
    url:
      "https://post-phinf.pstatic.net/MjAxOTEwMDJfMTk2/MDAxNTY5OTk2NTQyMTE4.oj6DIG-f-6AR8rAvKLWsha89zXu2V-YgYNztYd_jtosg.z0C8hh-Atl30a93kB5Zj4HTmS0pS2dHwXq9kvT6IGWQg.JPEG/7._%EB%AF%B8%EC%8B%A4.jpg?type=w1200",
  },
  {
    category: "CAFE",
    name: "미실",
    description: "역사와 감성을 담은 카페",
    url:
      "https://post-phinf.pstatic.net/MjAxOTEwMDJfMTk2/MDAxNTY5OTk2NTQyMTE4.oj6DIG-f-6AR8rAvKLWsha89zXu2V-YgYNztYd_jtosg.z0C8hh-Atl30a93kB5Zj4HTmS0pS2dHwXq9kvT6IGWQg.JPEG/7._%EB%AF%B8%EC%8B%A4.jpg?type=w1200",
  },
];

// One item component
// selected prop will be passed
const MenuItem = ({ category, text, description, url }) => {
  // const initColor = "#eb2f96";
  // const myFunction = () => {
  //   this.twoToneColor = "#00b992";
  // }

  const [iconState, seticonState] = useState(true);

  return (
    <div className="container">
      <div className="grid">
        <figure className="effect-kira">
          <img src={url} width="630px" height="400px"/>
          <figcaption>
            <h2>
              {category} <span>{text}</span>
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
          </figcaption>
        </figure>
      </div>
    </div>
  );
};

// All items component
// Important! add unique key
export const Menu = (list) =>
  list.map((el) => {
    const { category, name, description, url } = el;

    return (
      <MenuItem
        category={category}
        text={name}
        description={description}
        url={url}
        key={name}
      />
    );
  });

const selected = "item1";

class ScrollCard extends Component {
  constructor(props) {
    super(props);
    // call it again if items count changes
    this.menuItems = Menu(list, selected);
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

    return (
      <div className="App">
        <ScrollMenu data={menu} selected={selected} onSelect={this.onSelect} />
      </div>
    );
  }
}

export default ScrollCard;
