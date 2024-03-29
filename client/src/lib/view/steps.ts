import XgOverview from './content/XgOverview.svelte';
import FixturesOverview from './content/FixturesOverview.svelte';
import ShotsInBox from './content/ShotsInBox.svelte';
import FixturesInBox from './content/FixturesInBox.svelte';
import LeftRight from './content/LeftRight.svelte';
import FixturesLeftRight from './content/FixturesLeftRight.svelte';
import TimelineIntro from './content/TimelineIntro.svelte';
import HomeAway from './content/HomeAway.svelte';
import FixturesHomeAway from './content/FixturesHomeAway.svelte';
import Minutes from './content/Minutes.svelte';
import FixturesMinutes from './content/FixturesMinutes.svelte';
import Padding from './content/Padding.svelte';

import Pitch from '../Pitch.svelte';
import Heatmap from '../Heatmap.svelte';
import Matches from '../Matches.svelte';

export type Step = {
    content: any; // svelte element
    visuals: any[]; // svelte element
    shotLayout: 'default' | 'box' | 'leftright' | 'homeaway' | 'minutes';
    opponentsInfo: 'default' | 'leftright' | 'minutes';
};

export let steps: Step[] = [
    {
        content: XgOverview,
        visuals: [Pitch],
        shotLayout: 'default',
        opponentsInfo: 'default'
    },
    {
        content: FixturesOverview,
        visuals: [Heatmap, Pitch],
        shotLayout: 'default',
        opponentsInfo: 'default'
    },
    {
        content: ShotsInBox,
        visuals: [Pitch],
        shotLayout: 'box',
        opponentsInfo: 'default'
    },
    {
        content: FixturesInBox,
        visuals: [Pitch],
        shotLayout: 'box',
        opponentsInfo: 'default'
    },
    {
        content: LeftRight,
        visuals: [Pitch],
        shotLayout: 'leftright',
        opponentsInfo: 'default'
    },
    {
        content: FixturesLeftRight,
        visuals: [Pitch],
        shotLayout: 'leftright',
        opponentsInfo: 'leftright'
    },
    {
        content: TimelineIntro,
        visuals: [Matches],
        shotLayout: 'default',
        opponentsInfo: 'default'
    },
    {
        content: HomeAway,
        visuals: [Matches],
        shotLayout: 'homeaway',
        opponentsInfo: 'default'
    },
    {
        content: FixturesHomeAway,
        visuals: [Matches],
        shotLayout: 'homeaway',
        opponentsInfo: 'default'
    },
    {
        content: Minutes,
        visuals: [Matches],
        shotLayout: 'minutes',
        opponentsInfo: 'default'
    },
    {
        content: FixturesMinutes,
        visuals: [Matches],
        shotLayout: 'default',
        opponentsInfo: 'minutes'
    },
    {
        content: Padding,
        visuals: [Matches],
        shotLayout: 'default',
        opponentsInfo: 'minutes'
    }
];
