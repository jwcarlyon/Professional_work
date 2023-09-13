// import * as uiActionTypes from './uiActionTypes';

export function uiReducer(state, action) {
    switch(action.type)
    {
      case uiActionTypes.UI__START_ROTATION:
      case uiActionTypes.UI__STOP_ROTATION:
        return{ ...state, rotating: action.payload };
      default:
          return state;
    }
}
