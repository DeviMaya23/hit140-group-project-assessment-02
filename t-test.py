import init
import scipy.stats as st

def t_test():
        # Load the cleaned dataset

    df = init.get_cleaned_dataset2()
    dfNoRat = df[df['rat_arrival_number'] == 0]
    dfNoRat = dfNoRat['bat_landing_number'].to_numpy()
    dfWithRat = df[df['rat_arrival_number'] > 0]
    dfWithRat = dfWithRat['bat_landing_number'].to_numpy()

    # Separate the data into two groups:
    # 1. When no rats arrived (rat_arrival_number == 0)
    # 2. When rats did arrive (rat_arrival_number == 1)

    t_statistic, p_value = st.ttest_ind(dfNoRat, dfWithRat, equal_var=False, alternative='two-sided')

    print("Mean of dataset with rat arrivals", st.tmean(dfWithRat))
    print("Mean of dataset without rat arrivals", st.tmean(dfNoRat))
    print("P Value:", p_value)

    # Mean of dataset with rats = x_bar1
    # Mean of dataset without rats = x_bar2
    # Our null hypothesis is that rats are not affecting bats behaviour
    # when it comes to food. Therefore, the amount of bats landing
    # should be unaffected by rats.
    # H0 -> x_bar1 = x_bar2
    print("Null hypothesis: x_bar1 == x_bar2")
    print("P value is < 0.05, therefore the null hypothesis is invalid.")

t_test()
