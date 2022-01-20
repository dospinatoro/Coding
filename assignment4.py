# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:22:45 2022

@author: dany9
"""

import pandas as pd
import numpy as np

def blight_model():
    from sklearn.model_selection import train_test_split, GridSearchCV;
    from sklearn.preprocessing import LabelEncoder;
    from sklearn.ensemble import RandomForestRegressor;

    train = pd.read_csv('train.csv', encoding = "ISO-8859-1",low_memory=False);
    test = pd.read_csv('test.csv');
    addresses = pd.read_csv('addresses.csv');
    latlons = pd.read_csv('latlons.csv');

    train = train[train.country == 'USA'];
    test = test[test.country == 'USA'];
    train = train[np.isfinite(train['compliance'])];
    
    train = pd.merge(train, pd.merge(addresses, latlons, on='address'), on='ticket_id');
    test = pd.merge(test, pd.merge(addresses, latlons, on='address'), on='ticket_id');

    # drop all unnecessary columns
    train.drop(['agency_name', 'inspector_name', 'violator_name', 'non_us_str_code', 'violation_description', 
                'grafitti_status', 'state_fee', 'admin_fee', 'ticket_issued_date', 'hearing_date',
                'payment_amount', 'balance_due', 'payment_date', 'payment_status', 
                'collection_status', 'compliance_detail', 
                'violation_zip_code', 'country', 'address', 'violation_street_number',
                'violation_street_name', 'mailing_address_str_number', 'mailing_address_str_name', 
                'city', 'state', 'zip_code', 'address'], axis=1, inplace=True);


    etiquetas = LabelEncoder();
    etiquetas.fit(train['disposition'].append(test['disposition'], ignore_index=True));

    train['disposition'] = etiquetas.transform(train['disposition']);
    test['disposition'] = etiquetas.transform(test['disposition']);
    
    etiquetas.fit(train['violation_code'].append(test['violation_code'], ignore_index=True));
    
    
    train['violation_code'] = etiquetas.transform(train['violation_code']);
    test['violation_code'] = etiquetas.transform(test['violation_code']);
    train['lat'] = train['lat'].fillna(train['lat'].mean());
    train['lon'] = train['lon'].fillna(train['lon'].mean());
    test['lat'] = test['lat'].fillna(test['lat'].mean());
    test['lon'] = test['lon'].fillna(test['lon'].mean());
    columnas_tr = list(train.columns.values);
    columnas_tr.remove('compliance');
    test = test[columnas_tr];
    
    split=train.loc[:, train.columns != 'compliance'];
    X_train, X_test, y_train, y_test = train_test_split(split,train['compliance']);
    
    forest = RandomForestRegressor();
    forestAUC = GridSearchCV(forest, scoring='roc_auc', param_grid={'n_estimators': [25, 75], 'max_depth': [None, 20]});
    forestAUC.fit(X_train, y_train);
    #print(forest_auc.best_params_);
    #print( forest_auc.best_score_);
    prediccion=forestAUC.predict(test);
    resultado=pd.DataFrame(prediccion, test.ticket_id);
    
    return resultado


r=blight_model()