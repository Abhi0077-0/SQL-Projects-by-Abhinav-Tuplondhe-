use PortfolioP;

select * from CovidDeaths

select * from CovidVaccination

Select Location, date, total_cases, new_cases, total_deaths, population 
from CovidDeaths
order by 1,2


--Looking at Total Cases Vs Total deaths
-- Shows likelihood of dying if you contract covid in your country

Select Location, date, total_cases, new_cases, total_deaths, (CAST(total_deaths as float) / CAST(total_cases as float))*100 as Result
from CovidDeaths
order by 1,2

-- Looking at Total Cases vs Population
-- Shows what percentage of population got covid

Select Location, date, total_cases, new_cases, total_deaths, (CAST(total_cases as float) / CAST(population as float))*100 as Result
from CovidDeaths
order by 1,2


-- Showing Countries with Highest Death Count per Population

Select Location, MAX(cast(Total_deaths as int)) as TotalDeathCount
from CovidDeaths 
Where continent is not null
Group by Location
order by TotalDeathCount desc


-- Showing continents with the highest death count

Select continent, max(cast(Total_deaths as int)) as TotalDeathCount
from CovidDeaths 
Where continent is not null
Group by continent
order by TotalDeathCount desc


-- Looking for Countries with Highest Infection Rate compared to Population

Select Location, Population, Max(total_cases) as HighestInfectionCount, Max((total_deaths/population))*100 as PercentPopulationInfected
from CovidDeaths
Group by location, population
order by PercentPopulationInfected desc



-- Global Numbers


select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(New_cases)*100 as DeathPercentage
from CovidDeaths
where continent is not null
--Group by date
order by 1,2


-- Looking at Total Population vs Vaccinations


select DEA.continent, DEA.location, DEA.date, DEA.population, VAC.new_vaccinations, 
SUM(CAST(VAC.new_vaccinations AS BIGINT)) OVER (Partition by DEA.location Order by DEA.location, DEA.date ) as RollingPeopleVaccinated 
from CovidDeaths DEA
Join CovidVaccination VAC
	on DEA.location = VAC.location
	and DEA.date = VAC.date
Where DEA.continent is not null 
order by 2,3

--and VAC.new_vaccinations is not null
--order by DEA.date asc


-- Use CTE

With PopvsVac (Continent, location, date, population,new_vaccinations, RollingPeopleVaccinated) as
(
select DEA.continent, DEA.location, DEA.date, DEA.population, VAC.new_vaccinations, 
SUM(CAST(VAC.new_vaccinations AS BIGINT)) OVER (Partition by DEA.location Order by DEA.location, DEA.date ) as RollingPeopleVaccinated 
from CovidDeaths DEA
Join CovidVaccination VAC
	on DEA.location = VAC.location
	and DEA.date = VAC.date
Where DEA.continent is not null 
--order by 2,3
)

Select * , (RollingPeopleVaccinated/Population)*100
from PopvsVac


-- Temp Table

Drop Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated

(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
Select DEA.continent, DEA.location, DEA.date, DEA.population, VAC.new_vaccinations, 
SUM(CAST(VAC.new_vaccinations AS BIGINT)) OVER (Partition by DEA.location Order by DEA.location, DEA.date ) as RollingPeopleVaccinated
 
from CovidDeaths DEA
Join CovidVaccination VAC
	on DEA.location = VAC.location
	and DEA.date = VAC.date
--Where DEA.continent is not null 
--order by 2,3

Select * , (RollingPeopleVaccinated/Population)*100
from #PercentPopulationVaccinated


-- Creating view to store data for later visualizations

Create View PercentPopulationVaccinated as

Select DEA.continent, DEA.location, DEA.date, DEA.population, VAC.new_vaccinations, 
SUM(CAST(VAC.new_vaccinations AS BIGINT)) OVER (Partition by DEA.location Order by DEA.location, DEA.date ) as RollingPeopleVaccinated
 
from CovidDeaths DEA
Join CovidVaccination VAC
	on DEA.location = VAC.location
	and DEA.date = VAC.date
Where DEA.continent is not null 
--order by 2,3


Select *
From PercentPopulationVaccinated