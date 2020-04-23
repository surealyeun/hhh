import React from "react";
import { Link } from "react-router-dom";
import "./Card.scss";

const Place2 = ({ state }) => {
  const {
    id,
    store_name,
    description,
    address_see,
    address_gu,
    address_dong,
    url,
    latitude,
    longitude,
  } = state;
  
  return (
    <div className="box">
      <div>
        <Link
          to={{
            pathname: `/store/${id}`,
            state: {
              store_name,
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
            <img src="https://www.gyeongnam.go.kr/upload_data/board_data/BBS_0001505/20181204524232968.jpg" width="630px" height="400px" />
            <figcaption>
              <h2 style={{ color: "#fff" }}>
                <span className="inner-span">{store_name}</span>
              </h2>

              <p style={{ margin: "20px" }}>{description}</p>
            </figcaption>
          </figure>
        </Link>
      </div>
    </div>
  );
};

export default Place2;
