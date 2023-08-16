import * as formulaUnoActionTypes from './formulaUnoActionTypes';

export function formulaUnoReducer(state, action) {
  switch (action.type) {
    case formulaUnoActionTypes.CAROUSEL__NEXT:
      console.log("reducer next found.");
      return {
        ...state,
        index: next(state.index + 1)
      };
    case formulaUnoActionTypes.CAROUSEL__PREV:
      return {
        ...state,
        index: previous(state.index - 0)
      };
    default:
      return state;
  }
}
