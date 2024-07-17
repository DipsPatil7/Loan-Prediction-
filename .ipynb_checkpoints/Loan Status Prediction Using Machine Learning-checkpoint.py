{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('loan_prediction.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Display Top 5 Rows of The Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>loan_id</th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "      <th>loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>9600000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>29900000</td>\n",
       "      <td>96</td>\n",
       "      <td>Rural</td>\n",
       "      <td>778</td>\n",
       "      <td>1</td>\n",
       "      <td>2400000</td>\n",
       "      <td>17600000</td>\n",
       "      <td>22700000</td>\n",
       "      <td>8000000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>F</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4100000</td>\n",
       "      <td>4000000.0</td>\n",
       "      <td>12200000</td>\n",
       "      <td>324</td>\n",
       "      <td>Rural</td>\n",
       "      <td>417</td>\n",
       "      <td>0</td>\n",
       "      <td>2700000</td>\n",
       "      <td>2200000</td>\n",
       "      <td>8800000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>F</td>\n",
       "      <td>No</td>\n",
       "      <td>3</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>9100000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>29700000</td>\n",
       "      <td>48</td>\n",
       "      <td>Rural</td>\n",
       "      <td>506</td>\n",
       "      <td>0</td>\n",
       "      <td>7100000</td>\n",
       "      <td>4500000</td>\n",
       "      <td>33300000</td>\n",
       "      <td>12800000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>8200000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>30700000</td>\n",
       "      <td>24</td>\n",
       "      <td>Urban</td>\n",
       "      <td>467</td>\n",
       "      <td>0</td>\n",
       "      <td>18200000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>23300000</td>\n",
       "      <td>7900000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>F</td>\n",
       "      <td>Yes</td>\n",
       "      <td>5</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>9800000</td>\n",
       "      <td>2000000.0</td>\n",
       "      <td>24200000</td>\n",
       "      <td>300</td>\n",
       "      <td>Urban</td>\n",
       "      <td>382</td>\n",
       "      <td>0</td>\n",
       "      <td>12400000</td>\n",
       "      <td>8200000</td>\n",
       "      <td>29400000</td>\n",
       "      <td>5000000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   loan_id gender married  no_of_dependents     education self_employed  \\\n",
       "0        1      M     Yes                 2      Graduate            No   \n",
       "1        2      F     Yes                 0  Not Graduate           Yes   \n",
       "2        3      F      No                 3      Graduate            No   \n",
       "3        4      M     Yes                 3      Graduate            No   \n",
       "4        5      F     Yes                 5  Not Graduate           Yes   \n",
       "\n",
       "   income_annum  co_app_income  loan_amount  loan_term_months property_area  \\\n",
       "0       9600000      5500000.0     29900000                96         Rural   \n",
       "1       4100000      4000000.0     12200000               324         Rural   \n",
       "2       9100000      3500000.0     29700000                48         Rural   \n",
       "3       8200000      3500000.0     30700000                24         Urban   \n",
       "4       9800000      2000000.0     24200000               300         Urban   \n",
       "\n",
       "   cibil_score  credit_history  residential_assets_value  \\\n",
       "0          778               1                   2400000   \n",
       "1          417               0                   2700000   \n",
       "2          506               0                   7100000   \n",
       "3          467               0                  18200000   \n",
       "4          382               0                  12400000   \n",
       "\n",
       "   commercial_assets_value  luxury_assets_value  bank_asset_value loan_status  \n",
       "0                 17600000             22700000           8000000    Approved  \n",
       "1                  2200000              8800000           3300000    Rejected  \n",
       "2                  4500000             33300000          12800000    Rejected  \n",
       "3                  3300000             23300000           7900000    Rejected  \n",
       "4                  8200000             29400000           5000000    Rejected  "
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Check Last 5 Rows of The Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>loan_id</th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "      <th>loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>110989</th>\n",
       "      <td>110990</td>\n",
       "      <td>F</td>\n",
       "      <td>No</td>\n",
       "      <td>5</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1000000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>2300000</td>\n",
       "      <td>144</td>\n",
       "      <td>Semi-Urban</td>\n",
       "      <td>317</td>\n",
       "      <td>0</td>\n",
       "      <td>2800000</td>\n",
       "      <td>500000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>800000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110990</th>\n",
       "      <td>110991</td>\n",
       "      <td>F</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3300000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>11300000</td>\n",
       "      <td>264</td>\n",
       "      <td>Urban</td>\n",
       "      <td>559</td>\n",
       "      <td>1</td>\n",
       "      <td>4200000</td>\n",
       "      <td>2900000</td>\n",
       "      <td>11000000</td>\n",
       "      <td>1900000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110991</th>\n",
       "      <td>110992</td>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>6500000</td>\n",
       "      <td>2000000.0</td>\n",
       "      <td>23900000</td>\n",
       "      <td>120</td>\n",
       "      <td>Rural</td>\n",
       "      <td>457</td>\n",
       "      <td>0</td>\n",
       "      <td>1200000</td>\n",
       "      <td>12400000</td>\n",
       "      <td>18100000</td>\n",
       "      <td>7300000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110992</th>\n",
       "      <td>110993</td>\n",
       "      <td>F</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>4100000</td>\n",
       "      <td>4000000.0</td>\n",
       "      <td>12800000</td>\n",
       "      <td>348</td>\n",
       "      <td>Semi-Urban</td>\n",
       "      <td>780</td>\n",
       "      <td>1</td>\n",
       "      <td>8200000</td>\n",
       "      <td>700000</td>\n",
       "      <td>14100000</td>\n",
       "      <td>5800000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110993</th>\n",
       "      <td>110994</td>\n",
       "      <td>F</td>\n",
       "      <td>No</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>9200000</td>\n",
       "      <td>6000000.0</td>\n",
       "      <td>29700000</td>\n",
       "      <td>144</td>\n",
       "      <td>Urban</td>\n",
       "      <td>607</td>\n",
       "      <td>1</td>\n",
       "      <td>17800000</td>\n",
       "      <td>11800000</td>\n",
       "      <td>35700000</td>\n",
       "      <td>12000000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        loan_id gender married  no_of_dependents     education self_employed  \\\n",
       "110989   110990      F      No                 5      Graduate           Yes   \n",
       "110990   110991      F     Yes                 0  Not Graduate           Yes   \n",
       "110991   110992      M     Yes                 2  Not Graduate            No   \n",
       "110992   110993      F     Yes                 1  Not Graduate            No   \n",
       "110993   110994      F      No                 1      Graduate            No   \n",
       "\n",
       "        income_annum  co_app_income  loan_amount  loan_term_months  \\\n",
       "110989       1000000      5500000.0      2300000               144   \n",
       "110990       3300000      5500000.0     11300000               264   \n",
       "110991       6500000      2000000.0     23900000               120   \n",
       "110992       4100000      4000000.0     12800000               348   \n",
       "110993       9200000      6000000.0     29700000               144   \n",
       "\n",
       "       property_area  cibil_score  credit_history  residential_assets_value  \\\n",
       "110989    Semi-Urban          317               0                   2800000   \n",
       "110990         Urban          559               1                   4200000   \n",
       "110991         Rural          457               0                   1200000   \n",
       "110992    Semi-Urban          780               1                   8200000   \n",
       "110993         Urban          607               1                  17800000   \n",
       "\n",
       "        commercial_assets_value  luxury_assets_value  bank_asset_value  \\\n",
       "110989                   500000              3300000            800000   \n",
       "110990                  2900000             11000000           1900000   \n",
       "110991                 12400000             18100000           7300000   \n",
       "110992                   700000             14100000           5800000   \n",
       "110993                 11800000             35700000          12000000   \n",
       "\n",
       "       loan_status  \n",
       "110989    Rejected  \n",
       "110990    Approved  \n",
       "110991    Rejected  \n",
       "110992    Approved  \n",
       "110993    Approved  "
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(110994, 18)"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Rows 110994\n",
      "Number of Columns 18\n"
     ]
    }
   ],
   "source": [
    "print(\"Number of Rows\",data.shape[0])\n",
    "print(\"Number of Columns\",data.shape[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 110994 entries, 0 to 110993\n",
      "Data columns (total 18 columns):\n",
      " #   Column                    Non-Null Count   Dtype  \n",
      "---  ------                    --------------   -----  \n",
      " 0   loan_id                   110994 non-null  int64  \n",
      " 1   gender                    110994 non-null  object \n",
      " 2   married                   110994 non-null  object \n",
      " 3   no_of_dependents          110994 non-null  int64  \n",
      " 4   education                 110994 non-null  object \n",
      " 5   self_employed             110994 non-null  object \n",
      " 6   income_annum              110994 non-null  int64  \n",
      " 7   co_app_income             92332 non-null   float64\n",
      " 8   loan_amount               110994 non-null  int64  \n",
      " 9   loan_term_months          110994 non-null  int64  \n",
      " 10  property_area             110994 non-null  object \n",
      " 11  cibil_score               110994 non-null  int64  \n",
      " 12  credit_history            110994 non-null  int64  \n",
      " 13  residential_assets_value  110994 non-null  int64  \n",
      " 14  commercial_assets_value   110994 non-null  int64  \n",
      " 15  luxury_assets_value       110994 non-null  int64  \n",
      " 16  bank_asset_value          110994 non-null  int64  \n",
      " 17  loan_status               110994 non-null  object \n",
      "dtypes: float64(1), int64(11), object(6)\n",
      "memory usage: 15.2+ MB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Check Null Values In The Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "loan_id                         0\n",
       "gender                          0\n",
       "married                         0\n",
       "no_of_dependents                0\n",
       "education                       0\n",
       "self_employed                   0\n",
       "income_annum                    0\n",
       "co_app_income               18662\n",
       "loan_amount                     0\n",
       "loan_term_months                0\n",
       "property_area                   0\n",
       "cibil_score                     0\n",
       "credit_history                  0\n",
       "residential_assets_value        0\n",
       "commercial_assets_value         0\n",
       "luxury_assets_value             0\n",
       "bank_asset_value                0\n",
       "loan_status                     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "loan_id                      0.000000\n",
       "gender                       0.000000\n",
       "married                      0.000000\n",
       "no_of_dependents             0.000000\n",
       "education                    0.000000\n",
       "self_employed                0.000000\n",
       "income_annum                 0.000000\n",
       "co_app_income               16.813521\n",
       "loan_amount                  0.000000\n",
       "loan_term_months             0.000000\n",
       "property_area                0.000000\n",
       "cibil_score                  0.000000\n",
       "credit_history               0.000000\n",
       "residential_assets_value     0.000000\n",
       "commercial_assets_value      0.000000\n",
       "luxury_assets_value          0.000000\n",
       "bank_asset_value             0.000000\n",
       "loan_status                  0.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()*100 / len(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Handling The missing Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data.drop('loan_id',axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "      <th>loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>9600000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>29900000</td>\n",
       "      <td>96</td>\n",
       "      <td>Rural</td>\n",
       "      <td>778</td>\n",
       "      <td>1</td>\n",
       "      <td>2400000</td>\n",
       "      <td>17600000</td>\n",
       "      <td>22700000</td>\n",
       "      <td>8000000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender married  no_of_dependents education self_employed  income_annum  \\\n",
       "0      M     Yes                 2  Graduate            No       9600000   \n",
       "\n",
       "   co_app_income  loan_amount  loan_term_months property_area  cibil_score  \\\n",
       "0      5500000.0     29900000                96         Rural          778   \n",
       "\n",
       "   credit_history  residential_assets_value  commercial_assets_value  \\\n",
       "0               1                   2400000                 17600000   \n",
       "\n",
       "   luxury_assets_value  bank_asset_value loan_status  \n",
       "0             22700000           8000000    Approved  "
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [],
   "source": [
    "columns = ['gender','no_of_dependents','loan_amount','loan_term_months']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data.dropna(subset=columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender                       0.000000\n",
       "married                      0.000000\n",
       "no_of_dependents             0.000000\n",
       "education                    0.000000\n",
       "self_employed                0.000000\n",
       "income_annum                 0.000000\n",
       "co_app_income               16.813521\n",
       "loan_amount                  0.000000\n",
       "loan_term_months             0.000000\n",
       "property_area                0.000000\n",
       "cibil_score                  0.000000\n",
       "credit_history               0.000000\n",
       "residential_assets_value     0.000000\n",
       "commercial_assets_value      0.000000\n",
       "luxury_assets_value          0.000000\n",
       "bank_asset_value             0.000000\n",
       "loan_status                  0.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()*100 / len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Yes'"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['self_employed'].mode()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['self_employed'] =data['self_employed'].fillna(data['self_employed'].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender                       0.000000\n",
       "married                      0.000000\n",
       "no_of_dependents             0.000000\n",
       "education                    0.000000\n",
       "self_employed                0.000000\n",
       "income_annum                 0.000000\n",
       "co_app_income               16.813521\n",
       "loan_amount                  0.000000\n",
       "loan_term_months             0.000000\n",
       "property_area                0.000000\n",
       "cibil_score                  0.000000\n",
       "credit_history               0.000000\n",
       "residential_assets_value     0.000000\n",
       "commercial_assets_value      0.000000\n",
       "luxury_assets_value          0.000000\n",
       "bank_asset_value             0.000000\n",
       "loan_status                  0.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()*100 / len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['M', 'F'], dtype=object)"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['gender'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['No', 'Yes'], dtype=object)"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['self_employed'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['credit_history'].mode()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['credit_history'] =data['credit_history'].fillna(data['credit_history'].mode()[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender                       0.000000\n",
       "married                      0.000000\n",
       "no_of_dependents             0.000000\n",
       "education                    0.000000\n",
       "self_employed                0.000000\n",
       "income_annum                 0.000000\n",
       "co_app_income               16.813521\n",
       "loan_amount                  0.000000\n",
       "loan_term_months             0.000000\n",
       "property_area                0.000000\n",
       "cibil_score                  0.000000\n",
       "credit_history               0.000000\n",
       "residential_assets_value     0.000000\n",
       "commercial_assets_value      0.000000\n",
       "luxury_assets_value          0.000000\n",
       "bank_asset_value             0.000000\n",
       "loan_status                  0.000000\n",
       "dtype: float64"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()*100 / len(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. Handling Categorical Columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "      <th>loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>95451</th>\n",
       "      <td>M</td>\n",
       "      <td>No</td>\n",
       "      <td>4</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>2700000</td>\n",
       "      <td>4000000.0</td>\n",
       "      <td>6100000</td>\n",
       "      <td>96</td>\n",
       "      <td>Semi-Urban</td>\n",
       "      <td>677</td>\n",
       "      <td>1</td>\n",
       "      <td>100000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>6500000</td>\n",
       "      <td>3800000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94024</th>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4</td>\n",
       "      <td>Not Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>9000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>18100000</td>\n",
       "      <td>96</td>\n",
       "      <td>Urban</td>\n",
       "      <td>764</td>\n",
       "      <td>1</td>\n",
       "      <td>600000</td>\n",
       "      <td>16500000</td>\n",
       "      <td>20800000</td>\n",
       "      <td>11600000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54543</th>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>4</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>600000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>2300000</td>\n",
       "      <td>300</td>\n",
       "      <td>Urban</td>\n",
       "      <td>495</td>\n",
       "      <td>0</td>\n",
       "      <td>1700000</td>\n",
       "      <td>600000</td>\n",
       "      <td>2000000</td>\n",
       "      <td>300000</td>\n",
       "      <td>Rejected</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31099</th>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>No</td>\n",
       "      <td>400000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1200000</td>\n",
       "      <td>48</td>\n",
       "      <td>Rural</td>\n",
       "      <td>766</td>\n",
       "      <td>1</td>\n",
       "      <td>900000</td>\n",
       "      <td>300000</td>\n",
       "      <td>1200000</td>\n",
       "      <td>300000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47339</th>\n",
       "      <td>M</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1</td>\n",
       "      <td>Graduate</td>\n",
       "      <td>Yes</td>\n",
       "      <td>8300000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>32100000</td>\n",
       "      <td>300</td>\n",
       "      <td>Semi-Urban</td>\n",
       "      <td>814</td>\n",
       "      <td>1</td>\n",
       "      <td>18500000</td>\n",
       "      <td>2700000</td>\n",
       "      <td>28900000</td>\n",
       "      <td>7500000</td>\n",
       "      <td>Approved</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      gender married  no_of_dependents     education self_employed  \\\n",
       "95451      M      No                 4  Not Graduate            No   \n",
       "94024      M     Yes                 4  Not Graduate           Yes   \n",
       "54543      M     Yes                 4      Graduate           Yes   \n",
       "31099      M     Yes                 0      Graduate            No   \n",
       "47339      M     Yes                 1      Graduate           Yes   \n",
       "\n",
       "       income_annum  co_app_income  loan_amount  loan_term_months  \\\n",
       "95451       2700000      4000000.0      6100000                96   \n",
       "94024       9000000            NaN     18100000                96   \n",
       "54543        600000      3500000.0      2300000               300   \n",
       "31099        400000            NaN      1200000                48   \n",
       "47339       8300000            NaN     32100000               300   \n",
       "\n",
       "      property_area  cibil_score  credit_history  residential_assets_value  \\\n",
       "95451    Semi-Urban          677               1                    100000   \n",
       "94024         Urban          764               1                    600000   \n",
       "54543         Urban          495               0                   1700000   \n",
       "31099         Rural          766               1                    900000   \n",
       "47339    Semi-Urban          814               1                  18500000   \n",
       "\n",
       "       commercial_assets_value  luxury_assets_value  bank_asset_value  \\\n",
       "95451                  3300000              6500000           3800000   \n",
       "94024                 16500000             20800000          11600000   \n",
       "54543                   600000              2000000            300000   \n",
       "31099                   300000              1200000            300000   \n",
       "47339                  2700000             28900000           7500000   \n",
       "\n",
       "      loan_status  \n",
       "95451    Approved  \n",
       "94024    Approved  \n",
       "54543    Rejected  \n",
       "31099    Approved  \n",
       "47339    Approved  "
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['no_of_dependents'] =data['no_of_dependents'].replace(to_replace=\"3+\",value='4')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0, 3, 5, 4, 1])"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['no_of_dependents'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Approved', 'Rejected'], dtype=object)"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['loan_status'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['gender'] = data['gender'].map({'M':1,'F':0}).astype('int')\n",
    "data['married'] = data['married'].map({'Yes':1,'No':0}).astype('int')\n",
    "data['education'] = data['education'].map({'Graduate':1,'Not Graduate':0}).astype('int')\n",
    "data['self_employed'] = data['self_employed'].map({'Yes':1,'No':0}).astype('int')\n",
    "data['property_area'] = data['property_area'].map({'Rural':0,'Semi-Urban':2,'Urban':1}).astype('int')\n",
    "data['loan_status'] = data['loan_status'].map({'Approved':1,'Rejected':0}).astype('int')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "      <th>loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>9600000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>29900000</td>\n",
       "      <td>96</td>\n",
       "      <td>0</td>\n",
       "      <td>778</td>\n",
       "      <td>1</td>\n",
       "      <td>2400000</td>\n",
       "      <td>17600000</td>\n",
       "      <td>22700000</td>\n",
       "      <td>8000000</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4100000</td>\n",
       "      <td>4000000.0</td>\n",
       "      <td>12200000</td>\n",
       "      <td>324</td>\n",
       "      <td>0</td>\n",
       "      <td>417</td>\n",
       "      <td>0</td>\n",
       "      <td>2700000</td>\n",
       "      <td>2200000</td>\n",
       "      <td>8800000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>9100000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>29700000</td>\n",
       "      <td>48</td>\n",
       "      <td>0</td>\n",
       "      <td>506</td>\n",
       "      <td>0</td>\n",
       "      <td>7100000</td>\n",
       "      <td>4500000</td>\n",
       "      <td>33300000</td>\n",
       "      <td>12800000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>8200000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>30700000</td>\n",
       "      <td>24</td>\n",
       "      <td>1</td>\n",
       "      <td>467</td>\n",
       "      <td>0</td>\n",
       "      <td>18200000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>23300000</td>\n",
       "      <td>7900000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>9800000</td>\n",
       "      <td>2000000.0</td>\n",
       "      <td>24200000</td>\n",
       "      <td>300</td>\n",
       "      <td>1</td>\n",
       "      <td>382</td>\n",
       "      <td>0</td>\n",
       "      <td>12400000</td>\n",
       "      <td>8200000</td>\n",
       "      <td>29400000</td>\n",
       "      <td>5000000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4800000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>13500000</td>\n",
       "      <td>180</td>\n",
       "      <td>2</td>\n",
       "      <td>319</td>\n",
       "      <td>0</td>\n",
       "      <td>6800000</td>\n",
       "      <td>8300000</td>\n",
       "      <td>13700000</td>\n",
       "      <td>5100000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>8700000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>33000000</td>\n",
       "      <td>264</td>\n",
       "      <td>1</td>\n",
       "      <td>678</td>\n",
       "      <td>1</td>\n",
       "      <td>22500000</td>\n",
       "      <td>14800000</td>\n",
       "      <td>29200000</td>\n",
       "      <td>4300000</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5700000</td>\n",
       "      <td>4000000.0</td>\n",
       "      <td>15000000</td>\n",
       "      <td>180</td>\n",
       "      <td>2</td>\n",
       "      <td>382</td>\n",
       "      <td>0</td>\n",
       "      <td>13200000</td>\n",
       "      <td>5700000</td>\n",
       "      <td>11800000</td>\n",
       "      <td>6000000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>800000</td>\n",
       "      <td>6000000.0</td>\n",
       "      <td>2200000</td>\n",
       "      <td>324</td>\n",
       "      <td>1</td>\n",
       "      <td>782</td>\n",
       "      <td>1</td>\n",
       "      <td>1300000</td>\n",
       "      <td>800000</td>\n",
       "      <td>2800000</td>\n",
       "      <td>600000</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1100000</td>\n",
       "      <td>2000000.0</td>\n",
       "      <td>4300000</td>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>388</td>\n",
       "      <td>0</td>\n",
       "      <td>3200000</td>\n",
       "      <td>1400000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>1600000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  married  no_of_dependents  education  self_employed  income_annum  \\\n",
       "0       1        1                 2          1              0       9600000   \n",
       "1       0        1                 0          0              1       4100000   \n",
       "2       0        0                 3          1              0       9100000   \n",
       "3       1        1                 3          1              0       8200000   \n",
       "4       0        1                 5          0              1       9800000   \n",
       "5       0        0                 0          1              1       4800000   \n",
       "6       0        1                 5          1              0       8700000   \n",
       "7       1        0                 2          1              1       5700000   \n",
       "8       0        0                 0          1              1        800000   \n",
       "9       0        0                 5          0              0       1100000   \n",
       "\n",
       "   co_app_income  loan_amount  loan_term_months  property_area  cibil_score  \\\n",
       "0      5500000.0     29900000                96              0          778   \n",
       "1      4000000.0     12200000               324              0          417   \n",
       "2      3500000.0     29700000                48              0          506   \n",
       "3      3500000.0     30700000                24              1          467   \n",
       "4      2000000.0     24200000               300              1          382   \n",
       "5            NaN     13500000               180              2          319   \n",
       "6      5500000.0     33000000               264              1          678   \n",
       "7      4000000.0     15000000               180              2          382   \n",
       "8      6000000.0      2200000               324              1          782   \n",
       "9      2000000.0      4300000                48              1          388   \n",
       "\n",
       "   credit_history  residential_assets_value  commercial_assets_value  \\\n",
       "0               1                   2400000                 17600000   \n",
       "1               0                   2700000                  2200000   \n",
       "2               0                   7100000                  4500000   \n",
       "3               0                  18200000                  3300000   \n",
       "4               0                  12400000                  8200000   \n",
       "5               0                   6800000                  8300000   \n",
       "6               1                  22500000                 14800000   \n",
       "7               0                  13200000                  5700000   \n",
       "8               1                   1300000                   800000   \n",
       "9               0                   3200000                  1400000   \n",
       "\n",
       "   luxury_assets_value  bank_asset_value  loan_status  \n",
       "0             22700000           8000000            1  \n",
       "1              8800000           3300000            0  \n",
       "2             33300000          12800000            0  \n",
       "3             23300000           7900000            0  \n",
       "4             29400000           5000000            0  \n",
       "5             13700000           5100000            0  \n",
       "6             29200000           4300000            1  \n",
       "7             11800000           6000000            0  \n",
       "8              2800000            600000            1  \n",
       "9              3300000           1600000            0  "
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 8. Store Feature Matrix In X And Response (Target) In Vector y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.drop('loan_status',axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = data['loan_status']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         1\n",
       "1         0\n",
       "2         0\n",
       "3         0\n",
       "4         0\n",
       "         ..\n",
       "110989    0\n",
       "110990    1\n",
       "110991    0\n",
       "110992    1\n",
       "110993    1\n",
       "Name: loan_status, Length: 110994, dtype: int64"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 9. Feature Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "      <th>loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>9600000</td>\n",
       "      <td>5500000.0</td>\n",
       "      <td>29900000</td>\n",
       "      <td>96</td>\n",
       "      <td>0</td>\n",
       "      <td>778</td>\n",
       "      <td>1</td>\n",
       "      <td>2400000</td>\n",
       "      <td>17600000</td>\n",
       "      <td>22700000</td>\n",
       "      <td>8000000</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4100000</td>\n",
       "      <td>4000000.0</td>\n",
       "      <td>12200000</td>\n",
       "      <td>324</td>\n",
       "      <td>0</td>\n",
       "      <td>417</td>\n",
       "      <td>0</td>\n",
       "      <td>2700000</td>\n",
       "      <td>2200000</td>\n",
       "      <td>8800000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>9100000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>29700000</td>\n",
       "      <td>48</td>\n",
       "      <td>0</td>\n",
       "      <td>506</td>\n",
       "      <td>0</td>\n",
       "      <td>7100000</td>\n",
       "      <td>4500000</td>\n",
       "      <td>33300000</td>\n",
       "      <td>12800000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>8200000</td>\n",
       "      <td>3500000.0</td>\n",
       "      <td>30700000</td>\n",
       "      <td>24</td>\n",
       "      <td>1</td>\n",
       "      <td>467</td>\n",
       "      <td>0</td>\n",
       "      <td>18200000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>23300000</td>\n",
       "      <td>7900000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>9800000</td>\n",
       "      <td>2000000.0</td>\n",
       "      <td>24200000</td>\n",
       "      <td>300</td>\n",
       "      <td>1</td>\n",
       "      <td>382</td>\n",
       "      <td>0</td>\n",
       "      <td>12400000</td>\n",
       "      <td>8200000</td>\n",
       "      <td>29400000</td>\n",
       "      <td>5000000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  married  no_of_dependents  education  self_employed  income_annum  \\\n",
       "0       1        1                 2          1              0       9600000   \n",
       "1       0        1                 0          0              1       4100000   \n",
       "2       0        0                 3          1              0       9100000   \n",
       "3       1        1                 3          1              0       8200000   \n",
       "4       0        1                 5          0              1       9800000   \n",
       "\n",
       "   co_app_income  loan_amount  loan_term_months  property_area  cibil_score  \\\n",
       "0      5500000.0     29900000                96              0          778   \n",
       "1      4000000.0     12200000               324              0          417   \n",
       "2      3500000.0     29700000                48              0          506   \n",
       "3      3500000.0     30700000                24              1          467   \n",
       "4      2000000.0     24200000               300              1          382   \n",
       "\n",
       "   credit_history  residential_assets_value  commercial_assets_value  \\\n",
       "0               1                   2400000                 17600000   \n",
       "1               0                   2700000                  2200000   \n",
       "2               0                   7100000                  4500000   \n",
       "3               0                  18200000                  3300000   \n",
       "4               0                  12400000                  8200000   \n",
       "\n",
       "   luxury_assets_value  bank_asset_value  loan_status  \n",
       "0             22700000           8000000            1  \n",
       "1              8800000           3300000            0  \n",
       "2             33300000          12800000            0  \n",
       "3             23300000           7900000            0  \n",
       "4             29400000           5000000            0  "
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [],
   "source": [
    "cols = ['income_annum','co_app_income','loan_amount','loan_term_months']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import MinMaxScaler\n",
    "st = MinMaxScaler()\n",
    "\n",
    "X[cols]=st.fit_transform(X[cols])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>married</th>\n",
       "      <th>no_of_dependents</th>\n",
       "      <th>education</th>\n",
       "      <th>self_employed</th>\n",
       "      <th>income_annum</th>\n",
       "      <th>co_app_income</th>\n",
       "      <th>loan_amount</th>\n",
       "      <th>loan_term_months</th>\n",
       "      <th>property_area</th>\n",
       "      <th>cibil_score</th>\n",
       "      <th>credit_history</th>\n",
       "      <th>residential_assets_value</th>\n",
       "      <th>commercial_assets_value</th>\n",
       "      <th>luxury_assets_value</th>\n",
       "      <th>bank_asset_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.969072</td>\n",
       "      <td>0.875</td>\n",
       "      <td>0.755102</td>\n",
       "      <td>0.241379</td>\n",
       "      <td>0</td>\n",
       "      <td>778</td>\n",
       "      <td>1</td>\n",
       "      <td>2400000</td>\n",
       "      <td>17600000</td>\n",
       "      <td>22700000</td>\n",
       "      <td>8000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.402062</td>\n",
       "      <td>0.500</td>\n",
       "      <td>0.303571</td>\n",
       "      <td>0.896552</td>\n",
       "      <td>0</td>\n",
       "      <td>417</td>\n",
       "      <td>0</td>\n",
       "      <td>2700000</td>\n",
       "      <td>2200000</td>\n",
       "      <td>8800000</td>\n",
       "      <td>3300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.917526</td>\n",
       "      <td>0.375</td>\n",
       "      <td>0.750000</td>\n",
       "      <td>0.103448</td>\n",
       "      <td>0</td>\n",
       "      <td>506</td>\n",
       "      <td>0</td>\n",
       "      <td>7100000</td>\n",
       "      <td>4500000</td>\n",
       "      <td>33300000</td>\n",
       "      <td>12800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.824742</td>\n",
       "      <td>0.375</td>\n",
       "      <td>0.775510</td>\n",
       "      <td>0.034483</td>\n",
       "      <td>1</td>\n",
       "      <td>467</td>\n",
       "      <td>0</td>\n",
       "      <td>18200000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>23300000</td>\n",
       "      <td>7900000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.989691</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.609694</td>\n",
       "      <td>0.827586</td>\n",
       "      <td>1</td>\n",
       "      <td>382</td>\n",
       "      <td>0</td>\n",
       "      <td>12400000</td>\n",
       "      <td>8200000</td>\n",
       "      <td>29400000</td>\n",
       "      <td>5000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110989</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0.082474</td>\n",
       "      <td>0.875</td>\n",
       "      <td>0.051020</td>\n",
       "      <td>0.379310</td>\n",
       "      <td>2</td>\n",
       "      <td>317</td>\n",
       "      <td>0</td>\n",
       "      <td>2800000</td>\n",
       "      <td>500000</td>\n",
       "      <td>3300000</td>\n",
       "      <td>800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110990</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.319588</td>\n",
       "      <td>0.875</td>\n",
       "      <td>0.280612</td>\n",
       "      <td>0.724138</td>\n",
       "      <td>1</td>\n",
       "      <td>559</td>\n",
       "      <td>1</td>\n",
       "      <td>4200000</td>\n",
       "      <td>2900000</td>\n",
       "      <td>11000000</td>\n",
       "      <td>1900000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110991</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.649485</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.602041</td>\n",
       "      <td>0.310345</td>\n",
       "      <td>0</td>\n",
       "      <td>457</td>\n",
       "      <td>0</td>\n",
       "      <td>1200000</td>\n",
       "      <td>12400000</td>\n",
       "      <td>18100000</td>\n",
       "      <td>7300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110992</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.402062</td>\n",
       "      <td>0.500</td>\n",
       "      <td>0.318878</td>\n",
       "      <td>0.965517</td>\n",
       "      <td>2</td>\n",
       "      <td>780</td>\n",
       "      <td>1</td>\n",
       "      <td>8200000</td>\n",
       "      <td>700000</td>\n",
       "      <td>14100000</td>\n",
       "      <td>5800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110993</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.927835</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.750000</td>\n",
       "      <td>0.379310</td>\n",
       "      <td>1</td>\n",
       "      <td>607</td>\n",
       "      <td>1</td>\n",
       "      <td>17800000</td>\n",
       "      <td>11800000</td>\n",
       "      <td>35700000</td>\n",
       "      <td>12000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>110994 rows × 16 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        gender  married  no_of_dependents  education  self_employed  \\\n",
       "0            1        1                 2          1              0   \n",
       "1            0        1                 0          0              1   \n",
       "2            0        0                 3          1              0   \n",
       "3            1        1                 3          1              0   \n",
       "4            0        1                 5          0              1   \n",
       "...        ...      ...               ...        ...            ...   \n",
       "110989       0        0                 5          1              1   \n",
       "110990       0        1                 0          0              1   \n",
       "110991       1        1                 2          0              0   \n",
       "110992       0        1                 1          0              0   \n",
       "110993       0        0                 1          1              0   \n",
       "\n",
       "        income_annum  co_app_income  loan_amount  loan_term_months  \\\n",
       "0           0.969072          0.875     0.755102          0.241379   \n",
       "1           0.402062          0.500     0.303571          0.896552   \n",
       "2           0.917526          0.375     0.750000          0.103448   \n",
       "3           0.824742          0.375     0.775510          0.034483   \n",
       "4           0.989691          0.000     0.609694          0.827586   \n",
       "...              ...            ...          ...               ...   \n",
       "110989      0.082474          0.875     0.051020          0.379310   \n",
       "110990      0.319588          0.875     0.280612          0.724138   \n",
       "110991      0.649485          0.000     0.602041          0.310345   \n",
       "110992      0.402062          0.500     0.318878          0.965517   \n",
       "110993      0.927835          1.000     0.750000          0.379310   \n",
       "\n",
       "        property_area  cibil_score  credit_history  residential_assets_value  \\\n",
       "0                   0          778               1                   2400000   \n",
       "1                   0          417               0                   2700000   \n",
       "2                   0          506               0                   7100000   \n",
       "3                   1          467               0                  18200000   \n",
       "4                   1          382               0                  12400000   \n",
       "...               ...          ...             ...                       ...   \n",
       "110989              2          317               0                   2800000   \n",
       "110990              1          559               1                   4200000   \n",
       "110991              0          457               0                   1200000   \n",
       "110992              2          780               1                   8200000   \n",
       "110993              1          607               1                  17800000   \n",
       "\n",
       "        commercial_assets_value  luxury_assets_value  bank_asset_value  \n",
       "0                      17600000             22700000           8000000  \n",
       "1                       2200000              8800000           3300000  \n",
       "2                       4500000             33300000          12800000  \n",
       "3                       3300000             23300000           7900000  \n",
       "4                       8200000             29400000           5000000  \n",
       "...                         ...                  ...               ...  \n",
       "110989                   500000              3300000            800000  \n",
       "110990                  2900000             11000000           1900000  \n",
       "110991                 12400000             18100000           7300000  \n",
       "110992                   700000             14100000           5800000  \n",
       "110993                 11800000             35700000          12000000  \n",
       "\n",
       "[110994 rows x 16 columns]"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 10. Splitting The Dataset Into The Training Set And Test Set & Applying K-Fold Cross Validation "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.model_selection import cross_val_score\n",
    "from sklearn.metrics import accuracy_score\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def model_val(model,X,y):\n",
    "    X_train,X_test,y_train,y_test=train_test_split(X,y,\n",
    "                                                   test_size=0.20,\n",
    "                                                   random_state=42)\n",
    "    model.fit(X_train,y_train)\n",
    "    y_pred=model.predict(X_test)\n",
    "    print(f\"{model} accuracy is {accuracy_score(y_test,y_pred)}\")\n",
    "    \n",
    "    score = cross_val_score(model,X,y,cv=5)\n",
    "    print(f\"{model} Avg cross val score is {np.mean(score)}\")\n",
    "    model_df[model]=round(np.mean(score)*100,2)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.model_val(model, X, y)>"
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model_val"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 11. Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Input X contains NaN.\nLogisticRegression does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[163], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mlinear_model\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m LogisticRegression\n\u001b[1;32m      2\u001b[0m model \u001b[38;5;241m=\u001b[39m LogisticRegression()\n\u001b[0;32m----> 3\u001b[0m model_val(model,X,y)\n",
      "Cell \u001b[0;32mIn[161], line 5\u001b[0m, in \u001b[0;36mmodel_val\u001b[0;34m(model, X, y)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmodel_val\u001b[39m(model,X,y):\n\u001b[1;32m      2\u001b[0m     X_train,X_test,y_train,y_test\u001b[38;5;241m=\u001b[39mtrain_test_split(X,y,\n\u001b[1;32m      3\u001b[0m                                                    test_size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0.20\u001b[39m,\n\u001b[1;32m      4\u001b[0m                                                    random_state\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m42\u001b[39m)\n\u001b[0;32m----> 5\u001b[0m     model\u001b[38;5;241m.\u001b[39mfit(X_train,y_train)\n\u001b[1;32m      6\u001b[0m     y_pred\u001b[38;5;241m=\u001b[39mmodel\u001b[38;5;241m.\u001b[39mpredict(X_test)\n\u001b[1;32m      7\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mmodel\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m accuracy is \u001b[39m\u001b[38;5;132;01m{\u001b[39;00maccuracy_score(y_test,y_pred)\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/sklearn/linear_model/_logistic.py:1196\u001b[0m, in \u001b[0;36mLogisticRegression.fit\u001b[0;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[1;32m   1193\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m   1194\u001b[0m     _dtype \u001b[38;5;241m=\u001b[39m [np\u001b[38;5;241m.\u001b[39mfloat64, np\u001b[38;5;241m.\u001b[39mfloat32]\n\u001b[0;32m-> 1196\u001b[0m X, y \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_data(\n\u001b[1;32m   1197\u001b[0m     X,\n\u001b[1;32m   1198\u001b[0m     y,\n\u001b[1;32m   1199\u001b[0m     accept_sparse\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcsr\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m   1200\u001b[0m     dtype\u001b[38;5;241m=\u001b[39m_dtype,\n\u001b[1;32m   1201\u001b[0m     order\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m   1202\u001b[0m     accept_large_sparse\u001b[38;5;241m=\u001b[39msolver \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m [\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mliblinear\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msag\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msaga\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[1;32m   1203\u001b[0m )\n\u001b[1;32m   1204\u001b[0m check_classification_targets(y)\n\u001b[1;32m   1205\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclasses_ \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39munique(y)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/sklearn/base.py:584\u001b[0m, in \u001b[0;36mBaseEstimator._validate_data\u001b[0;34m(self, X, y, reset, validate_separately, **check_params)\u001b[0m\n\u001b[1;32m    582\u001b[0m         y \u001b[38;5;241m=\u001b[39m check_array(y, input_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mcheck_y_params)\n\u001b[1;32m    583\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 584\u001b[0m         X, y \u001b[38;5;241m=\u001b[39m check_X_y(X, y, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mcheck_params)\n\u001b[1;32m    585\u001b[0m     out \u001b[38;5;241m=\u001b[39m X, y\n\u001b[1;32m    587\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m no_val_X \u001b[38;5;129;01mand\u001b[39;00m check_params\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mensure_2d\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mTrue\u001b[39;00m):\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/sklearn/utils/validation.py:1106\u001b[0m, in \u001b[0;36mcheck_X_y\u001b[0;34m(X, y, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, estimator)\u001b[0m\n\u001b[1;32m   1101\u001b[0m         estimator_name \u001b[38;5;241m=\u001b[39m _check_estimator_name(estimator)\n\u001b[1;32m   1102\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[1;32m   1103\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mestimator_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m requires y to be passed, but the target y is None\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   1104\u001b[0m     )\n\u001b[0;32m-> 1106\u001b[0m X \u001b[38;5;241m=\u001b[39m check_array(\n\u001b[1;32m   1107\u001b[0m     X,\n\u001b[1;32m   1108\u001b[0m     accept_sparse\u001b[38;5;241m=\u001b[39maccept_sparse,\n\u001b[1;32m   1109\u001b[0m     accept_large_sparse\u001b[38;5;241m=\u001b[39maccept_large_sparse,\n\u001b[1;32m   1110\u001b[0m     dtype\u001b[38;5;241m=\u001b[39mdtype,\n\u001b[1;32m   1111\u001b[0m     order\u001b[38;5;241m=\u001b[39morder,\n\u001b[1;32m   1112\u001b[0m     copy\u001b[38;5;241m=\u001b[39mcopy,\n\u001b[1;32m   1113\u001b[0m     force_all_finite\u001b[38;5;241m=\u001b[39mforce_all_finite,\n\u001b[1;32m   1114\u001b[0m     ensure_2d\u001b[38;5;241m=\u001b[39mensure_2d,\n\u001b[1;32m   1115\u001b[0m     allow_nd\u001b[38;5;241m=\u001b[39mallow_nd,\n\u001b[1;32m   1116\u001b[0m     ensure_min_samples\u001b[38;5;241m=\u001b[39mensure_min_samples,\n\u001b[1;32m   1117\u001b[0m     ensure_min_features\u001b[38;5;241m=\u001b[39mensure_min_features,\n\u001b[1;32m   1118\u001b[0m     estimator\u001b[38;5;241m=\u001b[39mestimator,\n\u001b[1;32m   1119\u001b[0m     input_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mX\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m   1120\u001b[0m )\n\u001b[1;32m   1122\u001b[0m y \u001b[38;5;241m=\u001b[39m _check_y(y, multi_output\u001b[38;5;241m=\u001b[39mmulti_output, y_numeric\u001b[38;5;241m=\u001b[39my_numeric, estimator\u001b[38;5;241m=\u001b[39mestimator)\n\u001b[1;32m   1124\u001b[0m check_consistent_length(X, y)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/sklearn/utils/validation.py:921\u001b[0m, in \u001b[0;36mcheck_array\u001b[0;34m(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator, input_name)\u001b[0m\n\u001b[1;32m    915\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[1;32m    916\u001b[0m             \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFound array with dim \u001b[39m\u001b[38;5;132;01m%d\u001b[39;00m\u001b[38;5;124m. \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m expected <= 2.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    917\u001b[0m             \u001b[38;5;241m%\u001b[39m (array\u001b[38;5;241m.\u001b[39mndim, estimator_name)\n\u001b[1;32m    918\u001b[0m         )\n\u001b[1;32m    920\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m force_all_finite:\n\u001b[0;32m--> 921\u001b[0m         _assert_all_finite(\n\u001b[1;32m    922\u001b[0m             array,\n\u001b[1;32m    923\u001b[0m             input_name\u001b[38;5;241m=\u001b[39minput_name,\n\u001b[1;32m    924\u001b[0m             estimator_name\u001b[38;5;241m=\u001b[39mestimator_name,\n\u001b[1;32m    925\u001b[0m             allow_nan\u001b[38;5;241m=\u001b[39mforce_all_finite \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mallow-nan\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m    926\u001b[0m         )\n\u001b[1;32m    928\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m ensure_min_samples \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[1;32m    929\u001b[0m     n_samples \u001b[38;5;241m=\u001b[39m _num_samples(array)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/sklearn/utils/validation.py:161\u001b[0m, in \u001b[0;36m_assert_all_finite\u001b[0;34m(X, allow_nan, msg_dtype, estimator_name, input_name)\u001b[0m\n\u001b[1;32m    144\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m estimator_name \u001b[38;5;129;01mand\u001b[39;00m input_name \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mX\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mand\u001b[39;00m has_nan_error:\n\u001b[1;32m    145\u001b[0m     \u001b[38;5;66;03m# Improve the error message on how to handle missing values in\u001b[39;00m\n\u001b[1;32m    146\u001b[0m     \u001b[38;5;66;03m# scikit-learn.\u001b[39;00m\n\u001b[1;32m    147\u001b[0m     msg_err \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    148\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;132;01m{\u001b[39;00mestimator_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m does not accept missing values\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    149\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m encoded as NaN natively. For supervised learning, you might want\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    159\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#estimators-that-handle-nan-values\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m    160\u001b[0m     )\n\u001b[0;32m--> 161\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(msg_err)\n",
      "\u001b[0;31mValueError\u001b[0m: Input X contains NaN.\nLogisticRegression does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "model = LogisticRegression()\n",
    "model_val(model,X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 12. SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SVC() accuracy is 0.7927927927927928\n",
      "SVC() Avg cross val score is 0.7938902538902539\n"
     ]
    }
   ],
   "source": [
    "from sklearn import svm\n",
    "model = svm.SVC()\n",
    "model_val(model,X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 13. Decision Tree Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DecisionTreeClassifier() accuracy is 0.7747747747747747\n",
      "DecisionTreeClassifier() Avg cross val score is 0.7197870597870598\n"
     ]
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "model = DecisionTreeClassifier()\n",
    "model_val(model,X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 14. Random Forest Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RandomForestClassifier() accuracy is 0.7837837837837838\n",
      "RandomForestClassifier() Avg cross val score is 0.7757739557739558\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "model =RandomForestClassifier()\n",
    "model_val(model,X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 15. Gradient Boosting Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GradientBoostingClassifier() accuracy is 0.7927927927927928\n",
      "GradientBoostingClassifier() Avg cross val score is 0.774004914004914\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "model =GradientBoostingClassifier()\n",
    "model_val(model,X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 16. Hyperparameter Tuning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import RandomizedSearchCV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "log_reg_grid={\"C\":np.logspace(-4,4,20),\n",
    "             \"solver\":['liblinear']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "rs_log_reg=RandomizedSearchCV(LogisticRegression(),\n",
    "                   param_distributions=log_reg_grid,\n",
    "                  n_iter=20,cv=5,verbose=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 20 candidates, totalling 100 fits\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomizedSearchCV(cv=5, estimator=LogisticRegression(), n_iter=20,\n",
       "                   param_distributions={&#x27;C&#x27;: array([1.00000000e-04, 2.63665090e-04, 6.95192796e-04, 1.83298071e-03,\n",
       "       4.83293024e-03, 1.27427499e-02, 3.35981829e-02, 8.85866790e-02,\n",
       "       2.33572147e-01, 6.15848211e-01, 1.62377674e+00, 4.28133240e+00,\n",
       "       1.12883789e+01, 2.97635144e+01, 7.84759970e+01, 2.06913808e+02,\n",
       "       5.45559478e+02, 1.43844989e+03, 3.79269019e+03, 1.00000000e+04]),\n",
       "                                        &#x27;solver&#x27;: [&#x27;liblinear&#x27;]},\n",
       "                   verbose=True)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" ><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomizedSearchCV</label><div class=\"sk-toggleable__content\"><pre>RandomizedSearchCV(cv=5, estimator=LogisticRegression(), n_iter=20,\n",
       "                   param_distributions={&#x27;C&#x27;: array([1.00000000e-04, 2.63665090e-04, 6.95192796e-04, 1.83298071e-03,\n",
       "       4.83293024e-03, 1.27427499e-02, 3.35981829e-02, 8.85866790e-02,\n",
       "       2.33572147e-01, 6.15848211e-01, 1.62377674e+00, 4.28133240e+00,\n",
       "       1.12883789e+01, 2.97635144e+01, 7.84759970e+01, 2.06913808e+02,\n",
       "       5.45559478e+02, 1.43844989e+03, 3.79269019e+03, 1.00000000e+04]),\n",
       "                                        &#x27;solver&#x27;: [&#x27;liblinear&#x27;]},\n",
       "                   verbose=True)</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" ><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" ><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomizedSearchCV(cv=5, estimator=LogisticRegression(), n_iter=20,\n",
       "                   param_distributions={'C': array([1.00000000e-04, 2.63665090e-04, 6.95192796e-04, 1.83298071e-03,\n",
       "       4.83293024e-03, 1.27427499e-02, 3.35981829e-02, 8.85866790e-02,\n",
       "       2.33572147e-01, 6.15848211e-01, 1.62377674e+00, 4.28133240e+00,\n",
       "       1.12883789e+01, 2.97635144e+01, 7.84759970e+01, 2.06913808e+02,\n",
       "       5.45559478e+02, 1.43844989e+03, 3.79269019e+03, 1.00000000e+04]),\n",
       "                                        'solver': ['liblinear']},\n",
       "                   verbose=True)"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_log_reg.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8047829647829647"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_log_reg.best_score_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'solver': 'liblinear', 'C': 0.23357214690901212}"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_log_reg.best_params_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "svc_grid = {'C':[0.25,0.50,0.75,1],\"kernel\":[\"linear\"]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "rs_svc=RandomizedSearchCV(svm.SVC(),\n",
    "                  param_distributions=svc_grid,\n",
    "                   cv=5,\n",
    "                   n_iter=20,\n",
    "                  verbose=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 4 candidates, totalling 20 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/model_selection/_search.py:305: UserWarning: The total space of parameters 4 is smaller than n_iter=20. Running 4 iterations. For exhaustive searches, use GridSearchCV.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomizedSearchCV(cv=5, estimator=SVC(), n_iter=20,\n",
       "                   param_distributions={&#x27;C&#x27;: [0.25, 0.5, 0.75, 1],\n",
       "                                        &#x27;kernel&#x27;: [&#x27;linear&#x27;]},\n",
       "                   verbose=True)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" ><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomizedSearchCV</label><div class=\"sk-toggleable__content\"><pre>RandomizedSearchCV(cv=5, estimator=SVC(), n_iter=20,\n",
       "                   param_distributions={&#x27;C&#x27;: [0.25, 0.5, 0.75, 1],\n",
       "                                        &#x27;kernel&#x27;: [&#x27;linear&#x27;]},\n",
       "                   verbose=True)</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-5\" type=\"checkbox\" ><label for=\"sk-estimator-id-5\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: SVC</label><div class=\"sk-toggleable__content\"><pre>SVC()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-6\" type=\"checkbox\" ><label for=\"sk-estimator-id-6\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVC</label><div class=\"sk-toggleable__content\"><pre>SVC()</pre></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomizedSearchCV(cv=5, estimator=SVC(), n_iter=20,\n",
       "                   param_distributions={'C': [0.25, 0.5, 0.75, 1],\n",
       "                                        'kernel': ['linear']},\n",
       "                   verbose=True)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_svc.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8066011466011467"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_svc.best_score_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'kernel': 'linear', 'C': 0.25}"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_svc.best_params_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  Random Forest Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-7\" type=\"checkbox\" checked><label for=\"sk-estimator-id-7\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "RandomForestClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "rf_grid={'n_estimators':np.arange(10,1000,10),\n",
    "  'max_features':['auto','sqrt'],\n",
    " 'max_depth':[None,3,5,10,20,30],\n",
    " 'min_samples_split':[2,5,20,50,100],\n",
    " 'min_samples_leaf':[1,2,5,10]\n",
    " }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "rs_rf=RandomizedSearchCV(RandomForestClassifier(),\n",
    "                  param_distributions=rf_grid,\n",
    "                   cv=5,\n",
    "                   n_iter=20,\n",
    "                  verbose=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 20 candidates, totalling 100 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n",
      "/home/vivek/anaconda3/lib/python3.11/site-packages/sklearn/ensemble/_forest.py:424: FutureWarning: `max_features='auto'` has been deprecated in 1.1 and will be removed in 1.3. To keep the past behaviour, explicitly set `max_features='sqrt'` or remove this parameter as it is also the default value for RandomForestClassifiers and ExtraTreesClassifiers.\n",
      "  warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomizedSearchCV(cv=5, estimator=RandomForestClassifier(), n_iter=20,\n",
       "                   param_distributions={&#x27;max_depth&#x27;: [None, 3, 5, 10, 20, 30],\n",
       "                                        &#x27;max_features&#x27;: [&#x27;auto&#x27;, &#x27;sqrt&#x27;],\n",
       "                                        &#x27;min_samples_leaf&#x27;: [1, 2, 5, 10],\n",
       "                                        &#x27;min_samples_split&#x27;: [2, 5, 20, 50,\n",
       "                                                              100],\n",
       "                                        &#x27;n_estimators&#x27;: array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110, 120, 130,\n",
       "       140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260,\n",
       "       270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390,\n",
       "       400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520,\n",
       "       530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,\n",
       "       660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780,\n",
       "       790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910,\n",
       "       920, 930, 940, 950, 960, 970, 980, 990])},\n",
       "                   verbose=True)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-8\" type=\"checkbox\" ><label for=\"sk-estimator-id-8\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomizedSearchCV</label><div class=\"sk-toggleable__content\"><pre>RandomizedSearchCV(cv=5, estimator=RandomForestClassifier(), n_iter=20,\n",
       "                   param_distributions={&#x27;max_depth&#x27;: [None, 3, 5, 10, 20, 30],\n",
       "                                        &#x27;max_features&#x27;: [&#x27;auto&#x27;, &#x27;sqrt&#x27;],\n",
       "                                        &#x27;min_samples_leaf&#x27;: [1, 2, 5, 10],\n",
       "                                        &#x27;min_samples_split&#x27;: [2, 5, 20, 50,\n",
       "                                                              100],\n",
       "                                        &#x27;n_estimators&#x27;: array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110, 120, 130,\n",
       "       140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260,\n",
       "       270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390,\n",
       "       400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520,\n",
       "       530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,\n",
       "       660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780,\n",
       "       790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910,\n",
       "       920, 930, 940, 950, 960, 970, 980, 990])},\n",
       "                   verbose=True)</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-9\" type=\"checkbox\" ><label for=\"sk-estimator-id-9\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-10\" type=\"checkbox\" ><label for=\"sk-estimator-id-10\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomizedSearchCV(cv=5, estimator=RandomForestClassifier(), n_iter=20,\n",
       "                   param_distributions={'max_depth': [None, 3, 5, 10, 20, 30],\n",
       "                                        'max_features': ['auto', 'sqrt'],\n",
       "                                        'min_samples_leaf': [1, 2, 5, 10],\n",
       "                                        'min_samples_split': [2, 5, 20, 50,\n",
       "                                                              100],\n",
       "                                        'n_estimators': array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110, 120, 130,\n",
       "       140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260,\n",
       "       270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390,\n",
       "       400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520,\n",
       "       530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,\n",
       "       660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780,\n",
       "       790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910,\n",
       "       920, 930, 940, 950, 960, 970, 980, 990])},\n",
       "                   verbose=True)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_rf.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8066175266175266"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_rf.best_score_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'n_estimators': 20,\n",
       " 'min_samples_split': 20,\n",
       " 'min_samples_leaf': 2,\n",
       " 'max_features': 'sqrt',\n",
       " 'max_depth': 20}"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_rf.best_params_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "## LogisticRegression score Before Hyperparameter Tuning: 80.48\n",
    "## LogisticRegression score after Hyperparameter Tuning: 80.48 \n",
    "    \n",
    "## ------------------------------------------------------\n",
    "## SVC score Before Hyperparameter Tuning: 79.38\n",
    "## SVC score after Hyperparameter Tuning: 80.66\n",
    "    \n",
    "## --------------------------------------------------------\n",
    "## RandomForestClassifier score Before Hyperparameter Tuning: 77.76\n",
    "## RandomForestClassifier score after Hyperparameter Tuning: 80.66 \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 17. Save The Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.drop('Loan_Status',axis=1)\n",
    "y = data['Loan_Status']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "rf = RandomForestClassifier(n_estimators=270,\n",
    " min_samples_split=5,\n",
    " min_samples_leaf=5,\n",
    " max_features='sqrt',\n",
    " max_depth=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-5 {color: black;background-color: white;}#sk-container-id-5 pre{padding: 0;}#sk-container-id-5 div.sk-toggleable {background-color: white;}#sk-container-id-5 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-5 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-5 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-5 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-5 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-5 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-5 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-5 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-5 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-5 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-5 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-5 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-5 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-5 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-5 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-5 div.sk-item {position: relative;z-index: 1;}#sk-container-id-5 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-5 div.sk-item::before, #sk-container-id-5 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-5 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-5 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-5 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-5 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-5 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-5 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-5 div.sk-label-container {text-align: center;}#sk-container-id-5 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-5 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-5\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier(max_depth=5, min_samples_leaf=5, min_samples_split=5,\n",
       "                       n_estimators=270)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-11\" type=\"checkbox\" checked><label for=\"sk-estimator-id-11\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier(max_depth=5, min_samples_leaf=5, min_samples_split=5,\n",
       "                       n_estimators=270)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestClassifier(max_depth=5, min_samples_leaf=5, min_samples_split=5,\n",
       "                       n_estimators=270)"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['loan_status_predict']"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "joblib.dump(rf,'loan_status_predict')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load('loan_status_predict')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame({\n",
    "    'Gender':1,\n",
    "    'Married':1,\n",
    "    'Dependents':2,\n",
    "    'Education':0,\n",
    "    'Self_Employed':0,\n",
    "    'ApplicantIncome':2889,\n",
    "    'CoapplicantIncome':0.0,\n",
    "    'LoanAmount':45,\n",
    "    'Loan_Amount_Term':180,\n",
    "    'Credit_History':0,\n",
    "    'Property_Area':1\n",
    "},index=[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Gender</th>\n",
       "      <th>Married</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>Education</th>\n",
       "      <th>Self_Employed</th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "      <th>Property_Area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2889</td>\n",
       "      <td>0.0</td>\n",
       "      <td>45</td>\n",
       "      <td>180</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Gender  Married  Dependents  Education  Self_Employed  ApplicantIncome  \\\n",
       "0       1        1           2          0              0             2889   \n",
       "\n",
       "   CoapplicantIncome  LoanAmount  Loan_Amount_Term  Credit_History  \\\n",
       "0                0.0          45               180               0   \n",
       "\n",
       "   Property_Area  \n",
       "0              1  "
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "result = model.predict(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loan Not Approved\n"
     ]
    }
   ],
   "source": [
    "if result==1:\n",
    "    print(\"Loan Approved\")\n",
    "else:\n",
    "    print(\"Loan Not Approved\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# GUI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import joblib\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def show_entry():\n",
    "    \n",
    "    p1 = float(e1.get())\n",
    "    p2 = float(e2.get())\n",
    "    p3 = float(e3.get())\n",
    "    p4 = float(e4.get())\n",
    "    p5 = float(e5.get())\n",
    "    p6 = float(e6.get())\n",
    "    p7 = float(e7.get())\n",
    "    p8 = float(e8.get())\n",
    "    p9 = float(e9.get())\n",
    "    p10 = float(e10.get())\n",
    "    p11 = float(e11.get())\n",
    "    \n",
    "    model = joblib.load('loan_status_predict')\n",
    "    df = pd.DataFrame({\n",
    "    'Gender':p1,\n",
    "    'Married':p2,\n",
    "    'Dependents':p3,\n",
    "    'Education':p4,\n",
    "    'Self_Employed':p5,\n",
    "    'ApplicantIncome':p6,\n",
    "    'CoapplicantIncome':p7,\n",
    "    'LoanAmount':p8,\n",
    "    'Loan_Amount_Term':p9,\n",
    "    'Credit_History':p10,\n",
    "    'Property_Area':p11\n",
    "},index=[0])\n",
    "    result = model.predict(df)\n",
    "    \n",
    "    if result == 1:\n",
    "        Label(master, text=\"Loan approved\").grid(row=31)\n",
    "    else:\n",
    "        Label(master, text=\"Loan Not Approved\").grid(row=31)\n",
    "        \n",
    "    \n",
    "master =Tk()\n",
    "master.title(\"Loan Status Prediction Using Machine Learning\")\n",
    "label = Label(master,text = \"Loan Status Prediction\",bg = \"black\",\n",
    "               fg = \"white\").grid(row=0,columnspan=2)\n",
    "\n",
    "Label(master,text = \"Gender [1:Male ,0:Female]\").grid(row=1)\n",
    "Label(master,text = \"Married [1:Yes,0:No]\").grid(row=2)\n",
    "Label(master,text = \"Dependents [1,2,3,4]\").grid(row=3)\n",
    "Label(master,text = \"Education [1.Graduated, 2.Non-Graduated]\").grid(row=4)\n",
    "Label(master,text = \"Self_Employed [1.Yes, 2.No]\").grid(row=5)\n",
    "Label(master,text = \"ApplicantIncome\").grid(row=6)\n",
    "Label(master,text = \"CoapplicantIncome\").grid(row=7)\n",
    "Label(master,text = \"LoanAmount\").grid(row=8)\n",
    "Label(master,text = \"Loan_Amount_Term\").grid(row=9)\n",
    "Label(master,text = \"Credit_History[1/0]\").grid(row=10)\n",
    "Label(master,text = \"Property_Area [1.Urban, 2.Rural]\").grid(row=11)\n",
    "\n",
    "\n",
    "e1 = Entry(master)\n",
    "e2 = Entry(master)\n",
    "e3 = Entry(master)\n",
    "e4 = Entry(master)\n",
    "e5 = Entry(master)\n",
    "e6 = Entry(master)\n",
    "e7 = Entry(master)\n",
    "e8 = Entry(master)\n",
    "e9 = Entry(master)\n",
    "e10 = Entry(master)\n",
    "e11 = Entry(master)\n",
    "\n",
    "\n",
    "e1.grid(row=1,column=1)\n",
    "e2.grid(row=2,column=1)\n",
    "e3.grid(row=3,column=1)\n",
    "e4.grid(row=4,column=1)\n",
    "e5.grid(row=5,column=1)\n",
    "e6.grid(row=6,column=1)\n",
    "e7.grid(row=7,column=1)\n",
    "e8.grid(row=8,column=1)\n",
    "e9.grid(row=9,column=1)\n",
    "e10.grid(row=10,column=1)\n",
    "e11.grid(row=11,column=1)\n",
    "\n",
    "Button(master,text=\"Predict\",command=show_entry).grid()\n",
    "\n",
    "mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
