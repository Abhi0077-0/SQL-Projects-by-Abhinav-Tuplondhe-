use PortfolioP;


 /*

 Cleaning Data in SQL QQueries

 */

 Select *
 From NashvilleHousing

 ----------------------------------------------------------------------------------------------------

 -- Standardize Date Format


 Select SaleDateConverted, CONVERT(Date, SaleDate)
 From NashvilleHousing

 Update NashvilleHousing
 SET SaleDate = CONVERT(Date, SaleDate)

 ALTER TABLE NashvilleHousing
 Add SaleDateConverted Date;

 Update NashvilleHousing
 SET SaleDateConverted = CONVERT(Date, SaleDate)

 -----------------------------------------------------------------------------------------------------

 -- Populate Property Address data

 Select PropertyAddress
 From NashvilleHousing
 Where PropertyAddress is null;

 Select A.ParcelID, A.PropertyAddress, B.ParcelID, B.PropertyAddress, ISNULL( A.PropertyAddress, B.PropertyAddress)
 From NashvilleHousing A
 JOIN NashvilleHousing B
 on A.ParcelID = B.ParcelID
 AND A.[UniqueID ] <> B.[UniqueID ]
 Where A.PropertyAddress is null;

 Update A
 SET PropertyAddress = ISNULL(A.PropertyAddress, B.PropertyAddress)
  From NashvilleHousing A
 JOIN NashvilleHousing B
 on A.ParcelID = B.ParcelID
 AND A.[UniqueID ] <> B.[UniqueID ]
 Where A.PropertyAddress is null;


 -------------------------------------------------------------------------------------------------------------------------------------

 -- Breaking out Address into Individual Columns (Address, City, State)

 Select PropertyAddress
 From NashvilleHousing


 Select
 SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1) As Address,
 SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+1, LEN(PropertyAddress)) As Address
 From NashvilleHousing

 ALTER TABLE NashvilleHousing
 Add PropertySplitAddress Nvarchar(255);

 Update NashvilleHousing
 Set PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)

 ALTER TABLE NashvilleHousing
 Add PropertySplitCity Nvarchar(255);

 Update NashvilleHousing
 Set PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+1, LEN(PropertyAddress))

 Select *
 from NashvilleHousing

 Select OwnerAddress
 from NashvilleHousing

 Select
 PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
 PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
 PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
 from NashvilleHousing
 Where OwnerName is not null

 ALTER TABLE NashvilleHousing
 Add OwnerSplitAddress Nvarchar(255);

 Update NashvilleHousing
 Set OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3);


 ALTER TABLE NashvilleHousing
 Add OwnerSplitCity Nvarchar(255);

 Update NashvilleHousing
 Set OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2);


 ALTER TABLE NashvilleHousing
 Add OwnerSplitState Nvarchar(255);

 Update NashvilleHousing
 Set OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1);

 Select *
 from NashvilleHousing
 Where OwnerName is not null


 ---------------------------------------------------------------------------------------------------------------------------

 -- Change Y and N to "Yes" and "No" in coloumn "Sold as Vacant".

 Select Distinct(SoldAsVacant), COUNT(SoldAsVacant)
 from NashvilleHousing
 Group by SoldAsVacant
 order by 2

 Select SoldAsVacant,
 CASE When SoldAsVacant = 'Y' THEN 'Yes'
	  When SoldAsVacant = 'N' THEN 'No'
	  ELSE SoldAsVacant 
	  END
from NashvilleHousing

Update NashvilleHousing
SET SoldAsVacant = 
(
	  CASE When SoldAsVacant = 'Y' THEN 'Yes'
	  When SoldAsVacant = 'N' THEN 'No'
	  ELSE SoldAsVacant 
	  END
)
from NashvilleHousing


--------------------------------------------------------------------------------------------------------------------------------------------

-- Remove Duplicates

WITH RowNumCTE as (
Select*,
	ROW_NUMBER() OVER(
	PARTITION BY ParcelID,
				PropertyAddress,
				SalePrice,
				SaleDate,
				LegalReference
				ORDER BY
					UniqueID
					) row_num
	
from NashvilleHousing
--order by ParcelID
)
Select * from RowNumCTE
Where row_num > 1
Order by PropertyAddress

-- To Delete Duplicate Data

DELETE
from RowNumCTE
Where row_num > 1




-----------------------------------------------------------------------------------------------------------------------------------

-- Delete Unused Columns

Select * 
from NashvilleHousing
where OwnerName is not null

ALTER TABLE NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate