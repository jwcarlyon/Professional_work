import * as formulaUnoActionTypes from './formulaUnoActionTypes';

export function next()
{
    return{
        type: formulaUnoActionTypes.CAROUSEL__NEXT
    };
}

export function prev()
{
    return{
        type: formulaUnoActionTypes.CAROUSEL__PREV
    };
}
