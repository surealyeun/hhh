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
            <img src="https://www.agoda.com/wp-content/uploads/2019/03/Best-restaurants-in-Seoul-Fine-dining-Jungsik-Seoul-Mingles-restaurant.jpg" />
            <h2>
                <span className="small">{category}</span>
                <br />
              <span>
                {store_name}
              </span>
            </h2>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Place;
