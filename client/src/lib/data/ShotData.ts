import type { Shot, SimpleShot } from '$client';


export class SimpleShotData {
    shots: number
    
    constructor(shots: SimpleShot[]) {
        this.shots = shots.length;
    }


export class ShotData extends SimpleShotData {
    constructor(shots: Shot[]) {
        super(shots as SimpleShot[]);

    }
}
