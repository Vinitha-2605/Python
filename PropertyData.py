import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib.pagesizes import letter

inputFile = pd.read_csv("PropertyData.csv");
print(inputFile);

groupLocation = inputFile.groupby(['Location']);
avgPriceandSquareFootage = groupLocation.agg({"Price": "mean", "Square Footage": "mean"}).reset_index();
groupProperty = inputFile.groupby(['PropertyType']);
avgNoofBedandBathrooms = groupProperty.agg({"Number of bedrooms": "mean", "Number of bathrooms": "mean"}).reset_index();

print(avgPriceandSquareFootage);
print(avgNoofBedandBathrooms);

output = inputFile.groupby(['Location', 'PropertyType']);

propertyData = output.agg({"Price": "mean", "Square Footage": "mean", "Number of bedrooms": "mean", 
                  "Number of bathrooms": "mean"}).reset_index();

data = [];

data.append(list(avgPriceandSquareFootage.columns))
for index, row in avgPriceandSquareFootage.iterrows():
    data.append(row);
data.append(" ");

data.append(list(avgNoofBedandBathrooms.columns))
for index, row in avgNoofBedandBathrooms.iterrows():
    data.append(row);
data.append(" ");

data.append(list(propertyData.columns))
for index, row in propertyData.iterrows():
    data.append(row);

pdf = SimpleDocTemplate("Property.pdf", pagesize = letter);
propertyDataTable= Table(data);
propertyDataList =[];
propertyDataList.append(propertyDataTable);
pdf.build(propertyDataList);







