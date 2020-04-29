import React from "react";
import { Link } from "react-router-dom";

const Place = ({ state }) => {
  const {
    id,
    store_name,
    category,
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
        <div className="image">
          <Link
            to={{
              pathname: `/store/${id}`,
              state: {
                id,
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
            <img src={url} />
            <h2>
              {category ? (
                <span className="small">{category}</span>
              ) : (
                <span className="small">음식점</span>
              )}
              <br />
              <span>{store_name}</span>
            </h2>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Place;
