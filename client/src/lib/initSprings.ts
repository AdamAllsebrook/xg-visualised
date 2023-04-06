import { spring } from 'svelte/motion';

const springConfig = {
    stiffness: 0.05,
    damping: 0.3,
    precision: 0.01,
};

export function initSprings(xs: number[], ys: number[]) {
    let tweenedX = spring(xs, springConfig);
    let tweenedY = spring(ys, springConfig);
    return [tweenedX, tweenedY];
}
