import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const ShippingPolicy = () => {
  return (
    <Container maxWidth="md">
      <Box mt={4} mb={4}>
        <Typography variant="h4" gutterBottom>
          Shipping Policy
        </Typography>

        <Typography variant="h6" gutterBottom>
          Order Processing
        </Typography>
        <Typography variant="body1" paragraph>
          Please allow 1-2 business days to process your order. You will receive an email once your order has been shipped.
        </Typography>

        <Typography variant="h6" gutterBottom>
          Shipping Options
        </Typography>
        <Typography variant="body1" paragraph>
          We offer two shipping options:
        </Typography>
        <Typography variant="body1" paragraph>
          1. **Standard Shipping (4-7 Business Days):** Available for all orders within the US and Canada.
        </Typography>
        <Typography variant="body1" paragraph>
          2. **Express Shipping (2-3 Business Days):** Available for a flat rate of $10. This option is also available for orders within the US and Canada.
        </Typography>

        <Typography variant="h6" gutterBottom>
          Shipping Destinations
        </Typography>
        <Typography variant="body1" paragraph>
          We currently ship to the United States and Canada only.
        </Typography>

        <Typography variant="h6" gutterBottom>
          Domestic Shipping Rates and Estimates
        </Typography>
        <Typography variant="body1" paragraph>
          Shipping charges for your order will be calculated and displayed at checkout. Standard shipping is free for orders over $50. Express shipping is available at $10 for faster delivery.
        </Typography>

        <Typography variant="h6" gutterBottom>
          International Shipping
        </Typography>
        <Typography variant="body1" paragraph>
          We do not offer international shipping outside of the US and Canada at this time.
        </Typography>

        <Typography variant="h6" gutterBottom>
          Refunds, Returns, and Exchanges
        </Typography>
        <Typography variant="body1" paragraph>
          We accept returns up to 30 days after delivery if the item is unused and in its original condition. In the event that your order arrives damaged, please email us at support@email.com with your order number and a photo of the item’s condition.
        </Typography>
      </Box>
    </Container>
  );
};

export default ShippingPolicy;
