import type { SimpleShot } from "$client";
import { SimpleShotData } from "./shotData";

export const key = Symbol();

export class LeagueShotsConceded {
    teamShots: Map<string, SimpleShot[]>;
    data: Map<string, SimpleShotData>;

    constructor(teamsShotsConceded: Record<string, SimpleShot[]>) {
        this.teamShots = new Map(Object.entries(teamsShotsConceded));
        this.data = new Map(
            Object.entries(teamsShotsConceded).map(([team, shots]) => [team, new SimpleShotData(shots)])
        );
    }
}
