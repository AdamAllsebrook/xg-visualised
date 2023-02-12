import { writable } from 'svelte/store';

export const matches = writable([]);
export const seasons = writable([]);
export const team = writable({
    name: ''
});