#!/usr/bin/env python3
"""Brain Trivia: a colourful neuroscience quiz for your terminal.

Run:  python trivia.py            (10 random questions)
      python trivia.py --n 15     (choose how many)
"""
import argparse
import random

PINK, LAV, MINT, PEACH, DIM, RESET = "\033[95m", "\033[94m", "\033[92m", "\033[93m", "\033[2m", "\033[0m"

QUESTIONS = [
    ("Roughly how many neurons are in the human brain?", ["86 million", "86 billion", "86 trillion", "860 billion"], 1, "About 86 billion, plus a similar number of non-neuronal cells."),
    ("Which neurotransmitter is most associated with reward prediction and motivation?", ["Dopamine", "GABA", "Acetylcholine", "Glycine"], 0, "Dopamine neurons signal reward prediction errors."),
    ("Which brain structure was famously damaged in patient H.M., leaving him unable to form new memories?", ["Cerebellum", "Hippocampus", "Amygdala", "Thalamus"], 1, "H.M. had both medial temporal lobes, including the hippocampus, removed in 1953."),
    ("Which cells wrap axons in myelin in the central nervous system?", ["Astrocytes", "Microglia", "Oligodendrocytes", "Schwann cells"], 2, "Schwann cells do the job in the peripheral nervous system."),
    ("Which brain wave band is classically linked to relaxed wakefulness with eyes closed?", ["Delta", "Alpha", "Beta", "Gamma"], 1, "Alpha is roughly 8-12 Hz."),
    ("Which brain region contains the majority of the brain's neurons?", ["Cerebral cortex", "Cerebellum", "Brainstem", "Hippocampus"], 1, "The tiny cerebellum packs in most of the neurons."),
    ("What is the main inhibitory neurotransmitter in the adult brain?", ["Glutamate", "Serotonin", "GABA", "Dopamine"], 2, "GABA calms down neural activity."),
    ("Which region is crucial for processing fear and emotional salience?", ["Amygdala", "Pons", "Occipital lobe", "Olfactory bulb"], 0, "The amygdala is a key node in fear conditioning."),
    ("Hubel and Wiesel won a Nobel Prize for discovering what in visual cortex?", ["Face cells", "Orientation-selective neurons", "Grid cells", "Mirror neurons"], 1, "They found cells that respond to edges at particular angles."),
    ("Grid cells, which help build a map of space, were discovered in which area?", ["Entorhinal cortex", "Motor cortex", "Cerebellum", "Hypothalamus"], 0, "The Mosers and colleagues found them in entorhinal cortex."),
    ("Which structure is the brain's master circadian clock?", ["Pineal gland", "Suprachiasmatic nucleus", "Pituitary", "Habenula"], 1, "The SCN sits just above the optic chiasm."),
    ("Roughly what fraction of the body's energy does the brain use?", ["About 2%", "About 5%", "About 20%", "About 50%"], 2, "Around 20%, from an organ that is ~2% of body weight."),
    ("'Neurons that fire together wire together' summarises whose idea?", ["Hebb", "Pavlov", "Broca", "Golgi"], 0, "Donald Hebb proposed the principle in 1949."),
    ("Who drew beautiful early diagrams of neurons and championed the neuron doctrine?", ["Camillo Golgi", "Santiago Ramon y Cajal", "Paul Broca", "Wilder Penfield"], 1, "Cajal's drawings are still admired today."),
    ("Damage to Broca's area typically disrupts what?", ["Vision", "Speech production", "Balance", "Smell"], 1, "Patients understand language but struggle to speak fluently."),
    ("What typically happens to a neuron's membrane potential at the peak of an action potential?", ["It becomes strongly negative", "It briefly becomes positive", "It stays at rest", "It drops to zero permanently"], 1, "Sodium influx pushes the inside of the cell briefly positive."),
]


def main():
    parser = argparse.ArgumentParser(description="Neuroscience trivia")
    parser.add_argument("--n", type=int, default=10)
    n = min(parser.parse_args().n, len(QUESTIONS))
    picks = random.sample(QUESTIONS, n)
    score = 0
    print(f"\n{PINK}  BRAIN TRIVIA{RESET}\n")
    for i, (q, options, answer, fact) in enumerate(picks, 1):
        print(f"{LAV}Q{i}/{n}{RESET}  {q}")
        for j, opt in enumerate(options):
            print(f"   {PEACH}{'ABCD'[j]}{RESET}) {opt}")
        while True:
            choice = input("  your answer: ").strip().upper()
            if choice and choice in "ABCD"[: len(options)]:
                break
        if "ABCD".index(choice) == answer:
            score += 1
            print(f"  {MINT}correct!{RESET} {DIM}{fact}{RESET}\n")
        else:
            print(f"  {PINK}nope{RESET} - it was {options[answer]}. {DIM}{fact}{RESET}\n")
    print(f"{MINT}Final score: {score}/{n}{RESET}")
    print("Galaxy brain!" if score == n else "Keep firing, keep wiring.")


if __name__ == "__main__":
    main()
