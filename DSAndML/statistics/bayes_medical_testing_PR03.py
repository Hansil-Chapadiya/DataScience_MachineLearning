"""
Bayes' Theorem Application: Medical Testing Problem
==================================================

Problem Statement:
A medical testing company has developed a new test for a disease that affects 1 in every 1,000 people.
- Disease prevalence: 1/1,000 = 0.001 (0.1%)
- False positive rate: 1% (test says positive when patient is healthy)
- False negative rate: 5% (test says negative when patient has disease)

Question: If a patient tests positive, what's the probability they actually have the disease?

This is a classic application of Bayes' Theorem in medical diagnostics.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fractions import Fraction

class BayesianMedicalTest:
    def __init__(self, disease_prevalence, false_positive_rate, false_negative_rate):
        """
        Initialize the medical test parameters

        Parameters:
        - disease_prevalence: P(Disease) - probability of having the disease in population
        - false_positive_rate: P(Test+|Healthy) - probability of testing positive when healthy
        - false_negative_rate: P(Test-|Disease) - probability of testing negative when diseased
        """
        self.disease_prevalence = disease_prevalence
        self.false_positive_rate = false_positive_rate
        self.false_negative_rate = false_negative_rate

        # Derived probabilities
        self.healthy_rate = 1 - disease_prevalence
        self.true_positive_rate = 1 - false_negative_rate  # Sensitivity
        self.true_negative_rate = 1 - false_positive_rate  # Specificity

    def calculate_bayes_probability(self):
        """
        Calculate P(Disease|Test+) using Bayes' Theorem

        Bayes' Theorem:
        P(Disease|Test+) = P(Test+|Disease) × P(Disease) / P(Test+)

        Where:
        P(Test+) = P(Test+|Disease) × P(Disease) + P(Test+|Healthy) × P(Healthy)
        """

        print("="*80)
        print("BAYES' THEOREM CALCULATION")
        print("="*80)

        # Given probabilities
        print("Given Information:")
        print(f"• Disease prevalence: P(Disease) = {self.disease_prevalence:.4f} = {Fraction(1, 1000)}")
        print(f"• Healthy rate: P(Healthy) = {self.healthy_rate:.4f} = {Fraction(999, 1000)}")
        print(f"• False positive rate: P(Test+|Healthy) = {self.false_positive_rate:.4f} = {self.false_positive_rate:.0%}")
        print(f"• False negative rate: P(Test-|Disease) = {self.false_negative_rate:.4f} = {self.false_negative_rate:.0%}")
        print(f"• True positive rate (Sensitivity): P(Test+|Disease) = {self.true_positive_rate:.4f} = {self.true_positive_rate:.0%}")
        print(f"• True negative rate (Specificity): P(Test-|Healthy) = {self.true_negative_rate:.4f} = {self.true_negative_rate:.0%}")

        print("\n" + "-"*60)
        print("STEP-BY-STEP CALCULATION")
        print("-"*60)

        # Step 1: Calculate P(Test+)
        print("Step 1: Calculate P(Test+) using Law of Total Probability")
        print("P(Test+) = P(Test+|Disease) × P(Disease) + P(Test+|Healthy) × P(Healthy)")

        prob_test_positive_given_disease = self.true_positive_rate * self.disease_prevalence
        prob_test_positive_given_healthy = self.false_positive_rate * self.healthy_rate
        prob_test_positive = prob_test_positive_given_disease + prob_test_positive_given_healthy

        print(f"P(Test+) = {self.true_positive_rate:.4f} × {self.disease_prevalence:.4f} + {self.false_positive_rate:.4f} × {self.healthy_rate:.4f}")
        print(f"P(Test+) = {prob_test_positive_given_disease:.6f} + {prob_test_positive_given_healthy:.6f}")
        print(f"P(Test+) = {prob_test_positive:.6f}")

        # Step 2: Apply Bayes' Theorem
        print("\nStep 2: Apply Bayes' Theorem")
        print("P(Disease|Test+) = P(Test+|Disease) × P(Disease) / P(Test+)")

        prob_disease_given_positive = (self.true_positive_rate * self.disease_prevalence) / prob_test_positive

        print(f"P(Disease|Test+) = {self.true_positive_rate:.4f} × {self.disease_prevalence:.4f} / {prob_test_positive:.6f}")
        print(f"P(Disease|Test+) = {prob_test_positive_given_disease:.6f} / {prob_test_positive:.6f}")
        print(f"P(Disease|Test+) = {prob_disease_given_positive:.6f}")

        print("\n" + "="*60)
        print("FINAL ANSWER")
        print("="*60)
        print(f"If a patient tests POSITIVE, the probability they actually have the disease is:")
        print(f"P(Disease|Test+) = {prob_disease_given_positive:.6f} = {prob_disease_given_positive:.4%}")
        print(f"This is approximately {prob_disease_given_positive:.2%} or about {Fraction(prob_disease_given_positive).limit_denominator(1000)}")

        return prob_disease_given_positive, prob_test_positive

    def create_contingency_table(self, population_size=100000):
        """
        Create a contingency table to visualize the problem
        """
        print(f"\n" + "="*60)
        print(f"CONTINGENCY TABLE (Population: {population_size:,})")
        print("="*60)

        # Calculate actual numbers
        diseased_population = int(population_size * self.disease_prevalence)
        healthy_population = population_size - diseased_population

        # True positives: diseased people who test positive
        true_positives = int(diseased_population * self.true_positive_rate)
        # False negatives: diseased people who test negative
        false_negatives = diseased_population - true_positives

        # False positives: healthy people who test positive
        false_positives = int(healthy_population * self.false_positive_rate)
        # True negatives: healthy people who test negative
        true_negatives = healthy_population - false_positives

        # Total positives and negatives
        total_positives = true_positives + false_positives
        total_negatives = false_negatives + true_negatives

        print(f"                    Disease Status")
        print(f"Test Result    Has Disease    Healthy    Total")
        print(f"Positive       {true_positives:8d}    {false_positives:7d}    {total_positives:5d}")
        print(f"Negative       {false_negatives:8d}    {true_negatives:7d}    {total_negatives:5d}")
        print(f"Total          {diseased_population:8d}    {healthy_population:7d}    {population_size:5d}")

        print(f"\nKey Insights:")
        print(f"• True Positives: {true_positives:,} people")
        print(f"• False Positives: {false_positives:,} people")
        print(f"• Among {total_positives:,} positive tests, only {true_positives:,} actually have the disease")
        print(f"• Positive Predictive Value: {true_positives}/{total_positives} = {true_positives/total_positives:.4%}")

        return true_positives, false_positives, false_negatives, true_negatives

    def visualize_results(self):
        """
        Create visualizations to illustrate the Bayesian analysis
        """
        # Calculate probabilities
        prob_disease_given_positive, prob_test_positive = self.calculate_bayes_probability()

        # Create visualization
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))

        # 1. Prior vs Posterior Probability
        categories = ['Prior P(Disease)', 'Posterior P(Disease|Test+)']
        probabilities = [self.disease_prevalence, prob_disease_given_positive]
        colors = ['lightblue', 'darkred']

        bars = axes[0,0].bar(categories, probabilities, color=colors, alpha=0.7, edgecolor='black')
        axes[0,0].set_title('Prior vs Posterior Probability', fontsize=14, fontweight='bold')
        axes[0,0].set_ylabel('Probability')
        axes[0,0].grid(True, alpha=0.3)

        # Add value labels on bars
        for bar, prob in zip(bars, probabilities):
            height = bar.get_height()
            axes[0,0].text(bar.get_x() + bar.get_width()/2., height + 0.001,
                         f'{prob:.4%}', ha='center', va='bottom', fontweight='bold')

        # 2. Test Performance Metrics
        metrics = ['Sensitivity\n(True Positive Rate)', 'Specificity\n(True Negative Rate)',
                  'False Positive Rate', 'False Negative Rate']
        values = [self.true_positive_rate, self.true_negative_rate,
                 self.false_positive_rate, self.false_negative_rate]
        colors = ['green', 'green', 'red', 'red']

        bars = axes[0,1].bar(metrics, values, color=colors, alpha=0.7, edgecolor='black')
        axes[0,1].set_title('Test Performance Metrics', fontsize=14, fontweight='bold')
        axes[0,1].set_ylabel('Rate')
        axes[0,1].tick_params(axis='x', rotation=45)
        axes[0,1].grid(True, alpha=0.3)

        # Add value labels
        for bar, val in zip(bars, values):
            height = bar.get_height()
            axes[0,1].text(bar.get_x() + bar.get_width()/2., height + 0.01,
                         f'{val:.1%}', ha='center', va='bottom', fontweight='bold')

        # 3. Population Breakdown (pie chart)
        tp, fp, fn, tn = self.create_contingency_table(100000)

        # Focus on positive tests
        positive_breakdown = [tp, fp]
        positive_labels = [f'True Positives\n{tp:,}', f'False Positives\n{fp:,}']
        colors_pie = ['lightgreen', 'lightcoral']

        wedges, texts, autotexts = axes[1,0].pie(positive_breakdown, labels=positive_labels,
                                                colors=colors_pie, autopct='%1.1f%%',
                                                startangle=90, explode=(0.1, 0))
        axes[1,0].set_title('Breakdown of Positive Tests\n(Out of 100,000 people)',
                           fontsize=14, fontweight='bold')

        # 4. Effect of Disease Prevalence
        prevalences = np.logspace(-4, -1, 50)  # From 0.01% to 10%
        posterior_probs = []

        for prev in prevalences:
            # Calculate posterior for each prevalence
            prob_pos = self.true_positive_rate * prev + self.false_positive_rate * (1 - prev)
            posterior = (self.true_positive_rate * prev) / prob_pos
            posterior_probs.append(posterior)

        axes[1,1].semilogx(prevalences * 100, np.array(posterior_probs) * 100,
                          'b-', linewidth=2, label='P(Disease|Test+)')
        axes[1,1].axvline(self.disease_prevalence * 100, color='red', linestyle='--',
                         linewidth=2, label=f'Current prevalence: {self.disease_prevalence:.1%}')
        axes[1,1].axhline(prob_disease_given_positive * 100, color='red', linestyle=':',
                         linewidth=2, label=f'Current posterior: {prob_disease_given_positive:.2%}')
        axes[1,1].set_xlabel('Disease Prevalence (%)')
        axes[1,1].set_ylabel('P(Disease|Test+) (%)')
        axes[1,1].set_title('Effect of Disease Prevalence on Posterior Probability',
                           fontsize=14, fontweight='bold')
        axes[1,1].grid(True, alpha=0.3)
        axes[1,1].legend()

        plt.tight_layout()
        plt.show()

    def sensitivity_analysis(self):
        """
        Perform sensitivity analysis on test parameters
        """
        print("\n" + "="*60)
        print("SENSITIVITY ANALYSIS")
        print("="*60)

        # Vary false positive rates
        false_pos_rates = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1]

        print("Effect of False Positive Rate on Posterior Probability:")
        print("False Positive Rate | P(Disease|Test+)")
        print("-" * 40)

        for fpr in false_pos_rates:
            prob_pos = self.true_positive_rate * self.disease_prevalence + fpr * self.healthy_rate
            posterior = (self.true_positive_rate * self.disease_prevalence) / prob_pos
            print(f"{fpr:15.1%} | {posterior:12.4%}")

        print(f"\nCurrent test (FPR = {self.false_positive_rate:.1%}): {self.calculate_bayes_probability()[0]:.4%}")

def main():
    """
    Main function to solve the medical testing problem
    """
    print("BAYESIAN MEDICAL TESTING ANALYSIS")
    print("=" * 80)
    print("Problem: Medical test with 0.1% disease prevalence")
    print("Test characteristics: 1% false positive rate, 5% false negative rate")
    print()

    # Initialize the medical test
    medical_test = BayesianMedicalTest(
        disease_prevalence=1/1000,  # 0.1%
        false_positive_rate=0.01,   # 1%
        false_negative_rate=0.05    # 5%
    )

    # Calculate the main result
    prob_disease_given_positive, _ = medical_test.calculate_bayes_probability()

    # Create contingency table
    medical_test.create_contingency_table(100000)

    # Perform sensitivity analysis
    medical_test.sensitivity_analysis()

    # Create visualizations
    medical_test.visualize_results()

    # Summary
    print("\n" + "="*80)
    print("SUMMARY AND INTERPRETATION")
    print("="*80)
    print("🎯 ANSWER: If a patient tests positive, there is only a")
    print(f"   {prob_disease_given_positive:.2%} chance they actually have the disease!")
    print()
    print("🤔 WHY IS IT SO LOW?")
    print("   This counterintuitive result occurs because:")
    print("   1. The disease is very rare (0.1% prevalence)")
    print("   2. Even with a 'good' test (99% specificity), false positives")
    print("      vastly outnumber true positives in rare diseases")
    print("   3. Base rate neglect: we must consider the prior probability")
    print()
    print("📊 PRACTICAL IMPLICATIONS:")
    print("   • This is why screening tests often require confirmation")
    print("   • Multiple tests or more specific tests may be needed")
    print("   • Understanding Bayes' theorem is crucial in medical diagnosis")
    print("   • The test is still valuable for ruling OUT disease (high NPV)")

if __name__ == "__main__":
    main()