import type { SimpleShot } from "$client";
import { SimpleShotData } from "./shotData";

export const key = Symbol();

export class LeagueShotsConceded {
    teams: Map<string, SimpleShotData>;

    constructor(teamsShotsConceded: Record<string, SimpleShot[]>) {
        this.teams = new Map(
            Object.entries(teamsShotsConceded).map(([team, shots]) => [team, new SimpleShotData(shots)])
        );
    }
}
