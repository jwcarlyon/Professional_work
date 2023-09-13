import * as driversActionTypes from './driversActionTypes';

export function driversReducer(state = null, action) {
  switch (action.type) {
      case driversActionTypes.DRIVERS__GET_STATS_FAILED:
        return {
          ...state,
          stats: "The Stig"
        };

      case driversActionTypes.DRIVERS__GET_STATS_SUCCESS:
        return {
          ...state,
          stats: action.stats
        };

      default:
        return state;
  }
}
