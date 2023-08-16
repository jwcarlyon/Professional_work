import * as uiActionTypes from './uiActionTypes';

export function startRotation()
{
    return{
        type: uiActionTypes.UI__START_ROTATION,
        payload: true
    };
}

export function stopRotation()
{
    return{
        type: uiActionTypes.UI__STOP_ROTATION,
        payload: false
    };
}
