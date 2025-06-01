from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from Data_cleaning import preprocessing

[x,y] = preprocessing()
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#Linear Regression
def Linear_Regression():
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    y_pred_lr = lr.predict(x_test)
    print("Linear Regression")
    print("r2 Score = ", r2_score(y_test,y_pred_lr))
    print("RMSE = ", np.sqrt(mean_squared_error(y_test,y_pred_lr)))

#Random Forest
def Random_forest():
    rf = RandomForestRegressor()
    rf.fit(x_train,y_train)
    y_pred_rf = rf.predict(x_test)
    print("Random Forest")
    print("r2 Score = ", r2_score(y_test,y_pred_rf))
    print("RMSE = ", np.sqrt(mean_squared_error(y_test,y_pred_rf)))


#Decision Tree
def Decision_tree():
    dt = DecisionTreeRegressor()
    dt.fit(x_train,y_train)
    y_pred_dt = dt.predict(x_test)
    print("Decision Tree")
    print("r2 Score = ", r2_score(y_test,y_pred_dt))
    print("RMSE = ", np.sqrt(mean_squared_error(y_test,y_pred_dt)))

#XGBoost
def XGB_regressor():
    xgbreg = XGBRegressor()
    xgbreg.fit(x_train,y_train)
    y_pred_xg = xgbreg.predict(x_test)
    print("XGBoost")
    print("r2 Score = ", r2_score(y_test,y_pred_xg))
    print("RMSE = ", np.sqrt(mean_squared_error(y_test,y_pred_xg)))