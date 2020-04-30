import React from "react";
import { Link } from "react-router-dom";

const Place = ({ state, area }) => {
  const { id, store_name, category, location_name, description, url } = state;

  return (
    <div className="box">
      <div>
        <div className="image">
          <Link to={store_name !== undefined ? `/store/${id}` : `/place/${id}`}>
            <img src={url} />
            <h2>
              <span className="small">
                {category !== undefined
                  ? category
                    ? category
                    : "먹으러가자!"
                  : "놀러가자!"}
              </span>
              <br />
              <span>
                {store_name !== undefined ? store_name : location_name}
              </span>
            </h2>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Place;
