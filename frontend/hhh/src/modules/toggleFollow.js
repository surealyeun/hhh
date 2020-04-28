const TOGGLE_TRUE = "toggleFollow/toggleTrue";
const TOGGLE_FALSE = "toggleFollow/toggleFalse";

export const toggleTrue = () => ({ type: TOGGLE_TRUE });
export const toggleFalse = () => ({ type: TOGGLE_FALSE });

const initialState = {
  toggle: "none",
};

function toggle(state = initialState, action) {
  switch (action.type) {
    case TOGGLE_TRUE:
      return {
        toggle: "block",
      };

    case TOGGLE_FALSE:
      return {
        toggle: "none",
      };

    default:
      return state;
  }
}

export default toggle;
