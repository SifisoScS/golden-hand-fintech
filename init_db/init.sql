-- Create Database
IF NOT EXISTS(SELECT name FROM master.dbo.sysdatabases WHERE name = 'GoldenHandFinTech')
CREATE DATABASE GoldenHandFinTech;
GO

USE GoldenHandFinTech;
GO

-- Users Table (Pillar 1: User Management)
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber NVARCHAR(20),
    PasswordHash NVARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    Address NVARCHAR(255),
    City NVARCHAR(50),
    Country NVARCHAR(50),
    PostalCode NVARCHAR(20),
    KYCStatus NVARCHAR(20) DEFAULT 'Pending',
    AccountStatus NVARCHAR(20) DEFAULT 'Active',
    CreatedAt DATETIME2 DEFAULT GETUTCDATE(),
    UpdatedAt DATETIME2 DEFAULT GETUTCDATE()
);
GO

-- Accounts Table (Pillar 2: Account Management)
CREATE TABLE Accounts (
    AccountID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    AccountNumber NVARCHAR(20) UNIQUE NOT NULL,
    AccountType NVARCHAR(20) NOT NULL, -- Savings, Checking, Investment, etc.
    Currency NVARCHAR(3) DEFAULT 'USD',
    CurrentBalance DECIMAL(18,2) DEFAULT 0.00,
    AvailableBalance DECIMAL(18,2) DEFAULT 0.00,
    AccountStatus NVARCHAR(20) DEFAULT 'Active',
    InterestRate DECIMAL(5,3) DEFAULT 0.000,
    OpenedDate DATETIME2 DEFAULT GETUTCDATE(),
    ClosedDate DATETIME2 NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- Transactions Table (Pillar 3: Transaction Engine)
CREATE TABLE Transactions (
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    AccountID INT NOT NULL,
    TransactionType NVARCHAR(20) NOT NULL, -- Deposit, Withdrawal, Transfer, Payment
    Amount DECIMAL(18,2) NOT NULL,
    Currency NVARCHAR(3) DEFAULT 'USD',
    Description NVARCHAR(255),
    TransactionDate DATETIME2 DEFAULT GETUTCDATE(),
    Status NVARCHAR(20) DEFAULT 'Completed', -- Pending, Completed, Failed
    ReferenceNumber NVARCHAR(50) UNIQUE,
    SourceAccountID INT NULL,
    DestinationAccountID INT NULL,
    MerchantName NVARCHAR(100),
    Category NVARCHAR(50), -- Food, Transportation, Entertainment, etc.
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);
GO

-- Investment Portfolios Table (Pillar 4: Wealth Management)
CREATE TABLE InvestmentPortfolios (
    PortfolioID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    PortfolioName NVARCHAR(100) NOT NULL,
    RiskTolerance NVARCHAR(20), -- Conservative, Moderate, Aggressive
    TotalValue DECIMAL(18,2) DEFAULT 0.00,
    CreatedDate DATETIME2 DEFAULT GETUTCDATE(),
    LastUpdated DATETIME2 DEFAULT GETUTCDATE(),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- Investment Assets Table
CREATE TABLE InvestmentAssets (
    AssetID INT IDENTITY(1,1) PRIMARY KEY,
    PortfolioID INT NOT NULL,
    AssetType NVARCHAR(50) NOT NULL, -- Stock, Bond, Crypto, ETF
    Symbol NVARCHAR(20),
    AssetName NVARCHAR(100) NOT NULL,
    Quantity DECIMAL(18,8) NOT NULL,
    PurchasePrice DECIMAL(18,2) NOT NULL,
    CurrentPrice DECIMAL(18,2) NOT NULL,
    PurchaseDate DATETIME2 NOT NULL,
    FOREIGN KEY (PortfolioID) REFERENCES InvestmentPortfolios(PortfolioID)
);
GO

-- AI Recommendations Table (Pillar 5: Financial AI)
CREATE TABLE AIRecommendations (
    RecommendationID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    RecommendationType NVARCHAR(50) NOT NULL, -- Investment, Savings, Budget
    Title NVARCHAR(200) NOT NULL,
    Description NVARCHAR(1000),
    ConfidenceScore DECIMAL(3,2), -- 0.00 to 1.00
    RiskLevel NVARCHAR(20),
    ExpectedReturn DECIMAL(5,2),
    TimeHorizon NVARCHAR(20), -- Short, Medium, Long
    CreatedDate DATETIME2 DEFAULT GETUTCDATE(),
    Status NVARCHAR(20) DEFAULT 'Active', -- Active, Implemented, Dismissed
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- Security and Fraud Detection Table
CREATE TABLE SecurityEvents (
    EventID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    EventType NVARCHAR(50) NOT NULL, -- Login, Transaction, ProfileChange
    EventDescription NVARCHAR(500),
    IPAddress NVARCHAR(45),
    UserAgent NVARCHAR(500),
    Location NVARCHAR(100),
    IsSuspicious BIT DEFAULT 0,
    RiskScore INT DEFAULT 0,
    EventTimestamp DATETIME2 DEFAULT GETUTCDATE(),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- Budgets Table
CREATE TABLE Budgets (
    BudgetID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    Category NVARCHAR(50) NOT NULL,
    MonthlyLimit DECIMAL(18,2) NOT NULL,
    CurrentSpending DECIMAL(18,2) DEFAULT 0.00,
    BudgetMonth DATE NOT NULL,
    CreatedDate DATETIME2 DEFAULT GETUTCDATE(),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
GO

-- Create Indexes for Performance
CREATE INDEX IX_Transactions_AccountID ON Transactions(AccountID);
CREATE INDEX IX_Transactions_Date ON Transactions(TransactionDate);
CREATE INDEX IX_Accounts_UserID ON Accounts(UserID);
CREATE INDEX IX_SecurityEvents_UserID ON SecurityEvents(UserID);
CREATE INDEX IX_AIRecommendations_UserID ON AIRecommendations(UserID);
GO

-- Insert Sample Data
INSERT INTO Users (FirstName, LastName, Email, PhoneNumber, PasswordHash, KYCStatus) 
VALUES 
('John', 'Davidson', 'john.davidson@globaltech.com', '+1-555-0101', 'hashed_password_1', 'Verified'),
('Sarah', 'Mitchell', 'sarah.mitchell@fintech.io', '+1-555-0102', 'hashed_password_2', 'Verified'),
('Robert', 'Kim', 'robert.kim@bankofasia.com', '+1-555-0103', 'hashed_password_3', 'Verified');
GO

INSERT INTO Accounts (UserID, AccountNumber, AccountType, CurrentBalance, AvailableBalance) 
VALUES 
(1, 'ACC001', 'Checking', 15000.00, 15000.00),
(1, 'ACC002', 'Savings', 50000.00, 50000.00),
(2, 'ACC003', 'Investment', 75000.00, 75000.00),
(3, 'ACC004', 'Business', 200000.00, 200000.00);
GO

-- Create Stored Procedures
CREATE PROCEDURE GetUserFinancialSummary
    @UserID INT
AS
BEGIN
    SELECT 
        u.FirstName,
        u.LastName,
        COUNT(a.AccountID) as TotalAccounts,
        SUM(a.CurrentBalance) as TotalBalance,
        COUNT(t.TransactionID) as RecentTransactions,
        (SELECT COUNT(*) FROM AIRecommendations WHERE UserID = @UserID AND Status = 'Active') as ActiveRecommendations
    FROM Users u
    LEFT JOIN Accounts a ON u.UserID = a.UserID
    LEFT JOIN Transactions t ON a.AccountID = t.AccountID AND t.TransactionDate >= DATEADD(day, -30, GETUTCDATE())
    WHERE u.UserID = @UserID
    GROUP BY u.UserID, u.FirstName, u.LastName;
END;
GO

PRINT 'Golden Hand FinTech database schema created successfully!';