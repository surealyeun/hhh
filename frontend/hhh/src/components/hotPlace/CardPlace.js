import React from "react";
import { Link } from "react-router-dom";
import "./Card.scss";

const Place = ({ state }) => {
  const {
    id,
    location_name,
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
      <div className="card">
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
          <img src="https://www.gyeongnam.go.kr/upload_data/board_data/BBS_0001505/20181204524232968.jpg" />
        </Link>
      </div>
    </div>
  );
};

export default Place;
