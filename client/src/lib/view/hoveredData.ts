export enum HoveredDataType {
    Shot,
    Fixture
}

export type HoveredData = {
    data: any,
    index: number,
    component: any, // I really tried to get this to be typed as a svelte component... 
    type: HoveredDataType
}

export const key = Symbol();
