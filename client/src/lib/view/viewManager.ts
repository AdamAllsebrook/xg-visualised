import { type Step, steps } from './steps';
import type { HoveredData } from './hoveredData';
import { writable, type Writable } from 'svelte/store';

export const viewKey = Symbol();

export class ViewManager {
    steps: Step[];
    currentStep: Writable<number | undefined> = writable(undefined);
    hoveredData: Writable<HoveredData | null> = writable(null);
    teamSelected: Writable<string | null> = writable(null);

    constructor() {
        this.steps = steps;
    }
}
