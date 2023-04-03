import XgOverview from './content/XgOverview.svelte';
import FixturesOverview from './content/FixturesOverview.svelte';
import ShotsInBox from './content/ShotsInBox.svelte';
import Padding from './content/Padding.svelte';

import Pitch from '../Pitch.svelte';
import Heatmap from '../Heatmap.svelte';

export type Step = {
    content: any; // svelte element
    visuals: any[]; // svelte element
};

export let steps: Step[] = [
    {
        content: XgOverview,
        visuals: [Pitch],
    },
    {
        content: FixturesOverview,
        visuals: [Heatmap, Pitch],
    },
    {
        content: ShotsInBox,
        visuals: [Pitch],
    },
    {
        content: Padding,
        visuals: [Pitch],
    },
];
