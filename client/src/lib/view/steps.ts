import XgOverview from './content/XgOverview.svelte';
import FixturesOverview from './content/FixturesOverview.svelte';
import ShotsInBox from './content/ShotsInBox.svelte';
import FixturesInBox from './content/FixturesInBox.svelte';
import Padding from './content/Padding.svelte';

import Pitch from '../Pitch.svelte';
import Heatmap from '../Heatmap.svelte';
import Matches from '../Matches.svelte';

export type Step = {
    content: any; // svelte element
    visuals: any[]; // svelte element
    shotLayout: 'default' | 'box';
};

export let steps: Step[] = [
    {
        content: XgOverview,
        visuals: [Pitch],
        shotLayout: 'default'
    },
    {
        content: FixturesOverview,
        visuals: [Heatmap, Pitch],
        shotLayout: 'default'
    },
    {
        content: ShotsInBox,
        visuals: [Pitch],
        shotLayout: 'box'
    },
    {
        content: FixturesInBox,
        visuals: [Pitch],
        shotLayout: 'box'
    },
    {
        content: Padding,
        visuals: [Pitch],
        shotLayout: 'default'
    },
];
